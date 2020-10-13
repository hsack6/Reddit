import numpy as np
from scipy.io import mmread
import pandas as pd
import seaborn as sns
import networkx as nx
import glob
import re
import os
import sys
from collections import defaultdict
sns.set(style='darkgrid')
sns.set_style(style='whitegrid')

# 一つ上の階層のmoduleをインポートできるようにする
current_dir = os.path.dirname(os.path.abspath("__file__"))
sys.path.append( str(current_dir) + '/../' )

from setting_param import MakeSample_link_prediction_appeared_InputDir
EXIST_TABLE = np.load(MakeSample_link_prediction_appeared_InputDir + '/exist_table.npy')

from setting_param import MakeSample_node_prediction_lost_InputDir # SubNxLost

from setting_param import Evaluation_graph_prediction_OutputDir as OutputDir

from setting_param import L
from setting_param import ratio_test
from setting_param import ratio_valid
from setting_param import all_node_num
from setting_param import n_expanded

from graph_prediction_IO import get_appeared_InputDirs # appeared link
from graph_prediction_IO import get_disappeared_InputDirs # disappeared link
from graph_prediction_IO import get_new_InputDirs # new link
from graph_prediction_IO import get_lost_InputDirs # lost node


def load_paths_from_dir(dir_path):
    # dir 以下のファイル名のリストを取得
    path_list = glob.glob(dir_path + "/*")
    # ソート (ゼロ埋めされていない数字の文字列のソート)
    path_list = np.array(sorted(path_list, key=lambda s: int(re.findall(r'\d+', s)[-1])))
    return path_list


def dev_test_split(all_idx, n_samples, ratio_test):
    n_test = int(n_samples * ratio_test)
    return all_idx[:-n_test], all_idx[-n_test:]


def train_valid_split(dev_idx, n_samples, ratio_valid):
    n_valid = int(n_samples * ratio_valid)
    return dev_idx[:-n_valid], dev_idx[-n_valid:]


def true_pred_mask_split(input_dir):
    paths = load_paths_from_dir(input_dir + '/output')
    true_ls = []
    pred_ls = []
    mask_ls = []
    for path in paths:
        if 'true' in path.split('/')[-1]:
            true_ls.append(path)
        elif 'pred' in path.split('/')[-1]:
            pred_ls.append(path)
        elif 'mask' in path.split('/')[-1]:
            mask_ls.append(path)
    return np.array(true_ls), np.array(pred_ls), np.array(mask_ls)


def load_output_data(true_paths, pred_paths, mask_paths, target_idx):
    y_true = []
    y_pred = []
    y_mask = []
    for idx in target_idx:
        true = mmread(true_paths[idx]).toarray()
        pred = mmread(pred_paths[idx]).toarray()
        mask = mmread(mask_paths[idx]).toarray()
        y_true.append(true.tolist())
        y_pred.append(pred.tolist())
        y_mask.append(mask.tolist())
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_mask = np.array(y_mask)
    return y_true, y_pred, y_mask


def get_true_pred_mask(InputDir, is_train, is_valid, is_test):
    true_paths, pred_paths, mask_paths = true_pred_mask_split(InputDir)
    n_samples = len(true_paths)
    all_idx = list(range(n_samples))
    dev_idx, test_idx = dev_test_split(all_idx, n_samples, ratio_test)
    train_idx, valid_idx = dev_test_split(dev_idx, n_samples, ratio_valid)

    if is_train:
        target_idx = train_idx
    elif is_valid:
        target_idx = valid_idx
    elif is_test:
        target_idx = test_idx

    y_true, y_pred, y_mask = load_output_data(true_paths, pred_paths, mask_paths, target_idx)
    return y_true, y_pred, y_mask


def get_predicted_num_list(predicted_num_list, is_train, is_valid, is_test):
    n_samples = len(predicted_num_list)
    all_idx = list(range(n_samples))
    dev_idx, test_idx = dev_test_split(all_idx, n_samples, ratio_test)
    train_idx, valid_idx = dev_test_split(dev_idx, n_samples, ratio_valid)

    if is_train:
        target_idx = train_idx
    elif is_valid:
        target_idx = valid_idx
    elif is_test:
        target_idx = test_idx

    return np.array(predicted_num_list)[target_idx]


def sort_pred(true_, pred_, coordinate_):
    t, p, c = true_, pred_, coordinate_
    c_idx = list(range(len(c)))
    tmp_for_sort = list(zip(t.tolist(), p.tolist(), c_idx))
    tmp_for_sort = list(zip(*sorted(tmp_for_sort, key=lambda x: -x[1])))
    t = np.array(tmp_for_sort[0])
    p = np.array(tmp_for_sort[1])
    c = c[list(tmp_for_sort[2])]
    return (t, p, c)


def edge_coordinate_subset_pred(c, p, n):
    c = np.array(c, dtype=int).tolist()
    p = p.tolist()
    targets = set()
    while len(targets) < n:
        if p[0] < 0.0001:
            break
        targets.add(frozenset(c.pop(0)))
        p.pop(0)
    return targets


def edge_coordinate_subset_true(c, t):
    c = np.array(c, dtype=int).tolist()
    targets = set()
    for i, edge in enumerate(np.array(t, dtype=int).tolist()):
        if edge == 1:
            targets.add(frozenset(c[i]))
    return targets


def calc_edge_recall_precision(y_true, y_pred, y_mask, predicted_edge_num_list, n_node):
    """
    coordinate                      : (n_node, n_node, 2)
    true                            : (n_node, n_node)
    pred                            : (n_node, n_node)
    mask                            : (n_node, n_node)
    true_                           : (n_candidate)
    pred_                           : (n_candidate)
    coordinate_                     : (n_candidate, 2)
    """
    # 座標配列を生成
    coordinate = np.zeros((n_node, n_node, 2))
    for row in range(coordinate.shape[0]):
        for column in range(coordinate.shape[1]):
            coordinate[row][column][0] = row
            coordinate[row][column][1] = column

    n_pred = 0
    n_true = 0
    n_true_and_pred = 0
    pred_set_list = []
    true_set_list = []

    for sample_idx in range(y_true.shape[0]):
        # true, predを取得
        true = y_true[sample_idx]
        pred = y_pred[sample_idx]
        # 予測された数を取得
        n = predicted_edge_num_list[sample_idx]
        # maskをかける
        mask = y_mask[sample_idx]
        true_ = true[0 < mask]
        pred_ = pred[0 < mask]
        coordinate_ = coordinate[0 < mask]
        # predの高い順にtrue_, pred_, coordinate_をソート
        true_, pred_, coordinate_ = sort_pred(true_, pred_, coordinate_)
        # coordinate_の上から順に予測された数のリンクを追加（※対称座標は除去=無向グラフ）、これが予測されたリンク集合となる。
        pred_set = edge_coordinate_subset_pred(coordinate_, pred_, n)
        # 正解のリンク集合を取得
        true_set = edge_coordinate_subset_true(coordinate_, true_)
        # 正解集合と予測集合、および積集合の要素をカウント
        n_pred += len(pred_set)
        n_true += len(true_set)
        n_true_and_pred += len(true_set & pred_set)
        # 正解集合と予測集合を保持
        pred_set_list.append(pred_set)
        true_set_list.append(true_set)
    recall = -1 if n_true == 0 else n_true_and_pred / n_true
    precision = -1 if n_pred == 0 else n_true_and_pred / n_pred
    return recall, precision, pred_set_list, true_set_list


def node_coordinate_subset_pred(c, p, n):
    c = np.array(c, dtype=int).tolist()
    p = p.tolist()
    targets = set()
    while len(targets) < n:
        if p[0] < 0.0001:
            break
        targets.add(c.pop(0))
        p.pop(0)
    return targets


def node_coordinate_subset_true(c, t):
    c = np.array(c, dtype=int).tolist()
    targets = set()
    for i, node in enumerate(np.array(t, dtype=int).tolist()):
        if node == 1:
            targets.add(c[i])
    return targets


def calc_node_recall_precision(y_true, y_pred, y_mask, predicted_node_num_list, n_node):
    """
    coordinate      : (n_node, 1, 1)
    true            : (n_node, 1)
    pred            : (n_node, 1)
    mask            : (n_node, 1)
    true_           : (n_candidate)
    pred_           : (n_candidate)
    coordinate_     : (n_candidate)
    """
    # 座標配列を生成
    coordinate = np.zeros((n_node, 1))
    for row in range(coordinate.shape[0]):
        coordinate[row][0] = row

    n_pred = 0
    n_true = 0
    n_true_and_pred = 0
    pred_set_list = []
    true_set_list = []

    for sample_idx in range(y_true.shape[0]):
        # true, predを取得
        true = y_true[sample_idx]
        pred = y_pred[sample_idx]
        # 予測された数を取得
        n = predicted_node_num_list[sample_idx]
        # maskをかける
        mask = y_mask[sample_idx]
        true_ = true[0 < mask]
        pred_ = pred[0 < mask]
        coordinate_ = coordinate[0 < mask]
        # predの高い順にtrue_, pred_, coordinate_をソート
        true_, pred_, coordinate_ = sort_pred(true_, pred_, coordinate_)
        # coordinate_の上から順に予測された数のノードを追加
        pred_set = node_coordinate_subset_pred(coordinate_, pred_, n)
        # 正解のリンク集合を取得
        true_set = node_coordinate_subset_true(coordinate_, true_)
        # 正解集合と予測集合、および積集合の要素をカウント
        n_pred += len(pred_set)
        n_true += len(true_set)
        n_true_and_pred += len(true_set & pred_set)
        # 正解集合と予測集合を保持
        pred_set_list.append(pred_set)
        true_set_list.append(true_set)
    recall = -1 if n_true == 0 else n_true_and_pred / n_true
    precision = -1 if n_pred == 0 else n_true_and_pred / n_pred
    return recall, precision, pred_set_list, true_set_list


def get_ts_list(InputDir, is_train, is_valid, is_test):
    true_paths, pred_paths, mask_paths = true_pred_mask_split(InputDir)
    n_samples = len(true_paths)
    all_idx = list(range(n_samples))
    dev_idx, test_idx = dev_test_split(all_idx, n_samples, ratio_test)
    train_idx, valid_idx = dev_test_split(dev_idx, n_samples, ratio_valid)

    if is_train:
        target_idx = train_idx
    elif is_valid:
        target_idx = valid_idx
    elif is_test:
        target_idx = test_idx

    ts_list = list(map(lambda x: x + L, target_idx))
    return ts_list


def TsSplit(ts, L):
    ts_train = [(ts + l) for l in range(L)]
    ts_test = ts_train[-1] + 1
    ts_all = ts_train.copy()
    ts_all.extend([ts_test])
    return ts_train, ts_test, ts_all


def SubNxLost(ts, lost_nodes):
    Nx = nx.from_numpy_matrix(np.load(MakeSample_node_prediction_lost_InputDir + '/adjacency' + str(ts - 1) + '.npy'))
    return nx.Graph(Nx.edges(lost_nodes))


def get_edge_connected_lost_node(probability_InputDir, pred_node_set_list, true_node_set_list):
    ts_list = get_ts_list(probability_InputDir, False, False, True)
    n_pred = 0
    n_true = 0
    n_true_and_pred = 0
    pred_edge_set_list = []
    true_edge_set_list = []

    for ts_idx, ts in enumerate(ts_list):
        ts_train, ts_test, ts_all = TsSplit(ts, L)
        true_edge_set = set()
        for edge0, edge1 in SubNxLost(ts_test, true_node_set_list[ts_idx]).edges:
            true_edge_set.add(frozenset([edge0, edge1]))
        pred_edge_set = set()
        for edge0, edge1 in SubNxLost(ts_test, pred_node_set_list[ts_idx]).edges:
            pred_edge_set.add(frozenset([edge0, edge1]))
        # 正解集合と予測集合、および積集合の要素をカウント
        n_pred += len(pred_edge_set)
        n_true += len(true_edge_set)
        n_true_and_pred += len(true_edge_set & pred_edge_set)
        # 正解集合と予測集合を保持
        pred_edge_set_list.append(pred_edge_set)
        true_edge_set_list.append(true_edge_set)
    recall = -1 if n_true == 0 else n_true_and_pred / n_true
    precision = -1 if n_pred == 0 else n_true_and_pred / n_pred
    f1_score = 2 * (precision * recall) / (precision + recall)
    print("recall: ", recall, "precision: ", precision, "f1: ", f1_score)
    return pred_edge_set_list, true_edge_set_list, recall, precision, f1_score


def get_component_result(component_type, probability_InputDir, num_InputDir, node_num):
    predicted_num_list = []
    for ts in range(L, EXIST_TABLE.shape[1] - L):
        predicted_num = int(np.load(num_InputDir + '/output/pred' + str(ts) + '.npy'))
        predicted_num_list.append(predicted_num)

    y_true, y_pred, y_mask = get_true_pred_mask(probability_InputDir, False, False, True)
    y_predicted_num = get_predicted_num_list(predicted_num_list, False, False, True)
    if component_type == "node":
        recall, precision, pred_set_list, true_set_list = calc_node_recall_precision(y_true, y_pred, y_mask, y_predicted_num, node_num)
    elif component_type == "edge":
        recall, precision, pred_set_list, true_set_list = calc_edge_recall_precision(y_true, y_pred, y_mask, y_predicted_num, node_num)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(num_InputDir)
    print(probability_InputDir)
    print("recall: ", recall, "precision: ", precision, "f1: ", f1_score)
    return pred_set_list, true_set_list, recall, precision, f1_score


def delete_lost_node(pred_set, lost_node_set):
    edge_list = []
    for edge in pred_set:
        e0 = list(edge)[0]
        e1 = list(edge)[1]
        if e0 in lost_node_set or e1 in lost_node_set:
            edge_list.append(edge)
    for edge in edge_list:
        if edge in pred_set:
            pred_set.remove(edge)
    return pred_set


def link_prediction(n_appeared, p_appeared, n_disappeared, p_disappeared, n_new, p_new, n_lost, p_lost):

    probability_appeared_InputDir, num_appeared_InputDir = get_appeared_InputDirs(p_appeared, n_appeared)
    appeared_edge_pred_set_list, appeared_edge_true_set_list, recall_appeared_edge, precision_appeared_edge, f1_score_appeared_edge = get_component_result("edge", probability_appeared_InputDir, num_appeared_InputDir, all_node_num)

    probability_disappeared_InputDir, num_disappeared_InputDir = get_disappeared_InputDirs(p_disappeared, n_disappeared)
    disappeared_edge_pred_set_list, disappeared_edge_true_set_list, recall_disappeared_edge, precision_disappeared_edge, f1_score_disappeared_edge = get_component_result("edge", probability_disappeared_InputDir, num_disappeared_InputDir, all_node_num)

    probability_new_InputDir, num_new_InputDir = get_new_InputDirs(p_new, n_new)
    new_edge_pred_set_list, new_edge_true_set_list, recall_new_edge, precision_new_edge, f1_score_new_edge = get_component_result("edge", probability_new_InputDir, num_new_InputDir, all_node_num + n_expanded)

    probability_lost_InputDir, num_lost_InputDir = get_lost_InputDirs(p_lost, n_lost)
    lost_node_pred_set_list, lost_node_true_set_list, recall_lost_node, precision_lost_node, f1_score_lost_node = get_component_result("node", probability_lost_InputDir, num_lost_InputDir, all_node_num)
    lost_edge_pred_set_list, lost_edge_true_set_list, recall_lost_edge, precision_lost_edge, f1_score_lost_edge = get_edge_connected_lost_node(probability_lost_InputDir, lost_node_pred_set_list, lost_node_true_set_list)

    # 総合結果を計算
    # 「tのlink集合 」 + 「appeared (link) 集合」+ 「new (link) 集合」- 「disappeared (link) 集合」- 「lost (link) 集合」
    ts_list = get_ts_list(probability_appeared_InputDir, False, False, True)
    true_set_list = [] # axis0:ts
    pred_set_list = [[] for _ in range(len(ts_list))] # axis0:ts, axis1:ON/OFF(component)
    n_true = 0
    n_pred = [0 for _ in range(16)]
    n_true_and_pred = [0 for _ in range(16)]
    for i, ts in enumerate(ts_list):
        ts_train, ts_test, ts_all = TsSplit(ts, L)
        t_edge_set = set()
        for edge in nx.from_numpy_matrix(np.load(MakeSample_node_prediction_lost_InputDir + '/adjacency' + str(ts_train[-1]) + '.npy')).edges:
            t_edge_set.add(frozenset({edge[0], edge[1]}))

        appeared_edge_pred_set = appeared_edge_pred_set_list[i]
        appeared_edge_true_set = appeared_edge_true_set_list[i]
        assert len(t_edge_set & appeared_edge_true_set) == 0, "tのlink集合とappeared(link)集合は被らない"
        assert len(t_edge_set & appeared_edge_pred_set) == 0, "tのlink集合とappeared(link)集合は被らない"

        disappeared_edge_pred_set = disappeared_edge_pred_set_list[i]
        disappeared_edge_true_set = disappeared_edge_true_set_list[i]
        assert len(t_edge_set & disappeared_edge_true_set) == len(disappeared_edge_true_set), "tのlink集合とdisappeared(link)集合は被るべき"
        assert len(t_edge_set & disappeared_edge_pred_set) == len(disappeared_edge_pred_set), "tのlink集合とdisappeared(link)集合は被るべき"

        new_edge_pred_set = new_edge_pred_set_list[i]
        new_edge_true_set = new_edge_true_set_list[i]
        assert len(t_edge_set & new_edge_true_set) == 0, "tのlink集合とnew(link)集合は被らない"
        assert len(t_edge_set & new_edge_pred_set) == 0, "tのlink集合とnew(link)集合は被らない"

        lost_node_pred_set = lost_node_pred_set_list[i]
        lost_node_true_set = lost_node_true_set_list[i]
        lost_edge_pred_set = lost_edge_pred_set_list[i]
        lost_edge_true_set = lost_edge_true_set_list[i]
        assert len(t_edge_set & lost_edge_true_set) == len(lost_edge_true_set), "tのlink集合とlost(link)集合は被るべき"
        assert len(t_edge_set & lost_edge_pred_set) == len(lost_edge_pred_set), "tのlink集合とlost(link)集合は被るべき"

        true_set = (((t_edge_set | appeared_edge_true_set) | new_edge_true_set) - disappeared_edge_true_set) - lost_edge_true_set
        pred_set = [set() for _ in range(16)]

        # appeared : disappeared : new : lost
        # 何もしない場合 0000
        pred_set[0] = t_edge_set
        # lostのみをbest methodにした時 0001
        pred_set[1] = t_edge_set - lost_edge_pred_set
        pred_set[1] = delete_lost_node(pred_set[1], lost_node_pred_set)
        # newのみをbest methodにした時 0010
        pred_set[2] = t_edge_set | new_edge_pred_set
        # lostとnewのみをbest methodにした時 0011
        pred_set[3] = (t_edge_set | new_edge_pred_set) - lost_edge_pred_set
        pred_set[3] = delete_lost_node(pred_set[3], lost_node_pred_set)
        # disappearedのみをbest methodにした時 0100
        pred_set[4] = t_edge_set - disappeared_edge_pred_set

        # disappearedのみの結果だとrepeat0の方が良いが総合結果ではrepeat0が負けてしまう
        # 原因 : repeat0以外メソッドのdisappeared予測にはlostで予測しきれなかった真のlost edgeが多目に含まれていると考えられる → disappeared 単体予測だとlost nodeの特徴も同時に捉えているっぽい。
        # test_set = t_edge_set - disappeared_edge_true_set
        # print(len(t_edge_set), len(disappeared_edge_pred_set), len(disappeared_edge_true_set), len(disappeared_edge_true_set & disappeared_edge_pred_set), len(pred_set[4]&true_set), len(pred_set[4]&test_set))
        # print(len(disappeared_edge_pred_set & lost_edge_true_set)) → 実際にSTGGNNの方がrepeat0より10倍ほど多い
        # repeat0の学習にlost nodeの確率も追加すれば良いのでは？ (→ repeat1)
        # ぶっちゃけ予測結果の確率だけでなくてgivenな属性も加えた方が良い気がする。

        # disappearedとlostをbest methodにした時 0101
        pred_set[5] = (t_edge_set - disappeared_edge_pred_set) - lost_edge_pred_set
        pred_set[5] = delete_lost_node(pred_set[5], lost_node_pred_set)
        # disappearedとnewをbest methodにした時 0110
        pred_set[6] = (t_edge_set | new_edge_pred_set) - disappeared_edge_pred_set
        # disappearedとnewとlostをbest methodにした時 0111
        pred_set[7] = ((t_edge_set | new_edge_pred_set) - disappeared_edge_pred_set) - lost_edge_pred_set
        pred_set[7] = delete_lost_node(pred_set[7], lost_node_pred_set)
        # appearedのみをbest methodにした時 1000
        pred_set[8] = t_edge_set | appeared_edge_pred_set
        # appearedとlostをbest methodにした時 1001
        pred_set[9] = (t_edge_set | appeared_edge_pred_set) - lost_edge_pred_set
        pred_set[9] = delete_lost_node(pred_set[9], lost_node_pred_set)
        # appearedとnewをbest methodにした時 1010
        pred_set[10] = (t_edge_set | appeared_edge_pred_set) | new_edge_pred_set
        # appearedとnewとlostをbest methodにした時 1011
        pred_set[11] = ((t_edge_set | appeared_edge_pred_set) | new_edge_pred_set) - lost_edge_pred_set
        pred_set[11] = delete_lost_node(pred_set[11], lost_node_pred_set)
        # appearedとdisappearedのみをbest methodにした時 1100
        pred_set[12] = (t_edge_set | appeared_edge_pred_set) - disappeared_edge_pred_set
        # appearedとdisappearedとlostのみをbest methodにした時 1101
        pred_set[13] = ((t_edge_set | appeared_edge_pred_set) - disappeared_edge_pred_set) - lost_edge_pred_set
        pred_set[13] = delete_lost_node(pred_set[13], lost_node_pred_set)
        # appearedとdisappearedとnewのみをbest methodにした時 1110
        pred_set[14] = ((t_edge_set | appeared_edge_pred_set) | new_edge_pred_set) - disappeared_edge_pred_set
        # appearedとdisappearedとnewとlostをbest methodにした時 1111
        pred_set[15] = (((t_edge_set | appeared_edge_pred_set) | new_edge_pred_set) - disappeared_edge_pred_set) - lost_edge_pred_set
        pred_set[15] = delete_lost_node(pred_set[15], lost_node_pred_set)

        n_true += len(true_set)
        true_set_list.append(true_set)
        for c_idx in range(16):
            n_pred[c_idx] += len(pred_set[c_idx])
            n_true_and_pred[c_idx] += len(true_set & pred_set[c_idx])
            pred_set_list[i].append(pred_set[c_idx])

    recall = [0 for _ in range(16)]
    precision = [0 for _ in range(16)]
    f1_score = [0 for _ in range(16)]

    for c_idx in range(16):
        recall[c_idx] = -1 if n_true == 0 else n_true_and_pred[c_idx] / n_true
        precision[c_idx] = -1 if n_pred[c_idx] == 0 else n_true_and_pred[c_idx] / n_pred[c_idx]
        f1_score[c_idx] = 2 * (precision[c_idx] * recall[c_idx]) / (precision[c_idx] + recall[c_idx])
        print("Result", c_idx)
        print(recall[c_idx], precision[c_idx], f1_score[c_idx])

    eval_list = ['appeared', 'disappeared', 'new', 'lost', 'overall(baseline)', 'overall(lost)', 'overall(new)', 'overall(new & lost)', 'overall(disappeared)', 'overall(disappeared & lost)', 'overall(disappeared & new)', 'overall(disappeared & new & lost)', 'overall(appeared)', 'overall(appeared & lost)', 'overall(appeared & new)', 'overall(appeared & new & lost)', 'overall(appeared & disappeared)', 'overall(appeared & disappeared & lost)', 'overall(appeared & disappeared & new)', 'overall(appeared & disappeared & new & lost)']
    recall_list = sum([[recall_appeared_edge], [recall_disappeared_edge], [recall_new_edge], [recall_lost_edge], recall], [])
    precision_list = sum([[precision_appeared_edge], [precision_disappeared_edge], [precision_new_edge], [precision_lost_edge], precision], [])
    f1_score_list = sum([[f1_score_appeared_edge], [f1_score_disappeared_edge], [f1_score_new_edge], [f1_score_lost_edge], f1_score], [])

    os.makedirs(OutputDir, exist_ok=True)
    result_dic = {" ": eval_list, "recall": recall_list, "precision": precision_list, "f1": f1_score_list}
    df = pd.DataFrame(result_dic)
    df = df[[" ", "recall", "precision", "f1"]]
    df.to_csv(OutputDir + '/link_prediction_result-' + n_appeared + '-' + p_appeared + '-' + n_disappeared + '-' + p_disappeared + '-' + n_new + '-' + p_new + '-' + n_lost + '-' + p_lost + '.csv')


# link_prediction(n_appeared, p_appeared, n_disappeared, p_disappeared,  n_new,                    p_new, n_lost,  p_lost)
link_prediction(      "LSTM",   "STGGNN",        "LSTM",      "repeat0", "LSTM", "COSSIMMLP_Baseline_mix", "LSTM", "STGGNN")