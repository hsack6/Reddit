import numpy as np
import os
import sys
import networkx as nx
from scipy.sparse import lil_matrix
from scipy.io import mmwrite, mmread

# 一つ上の階層のmoduleをインポートできるようにする
current_dir = os.path.dirname(os.path.abspath("__file__"))
sys.path.append( str(current_dir) + '/../' )

from setting_param import MakeSample_repeat2_node_prediction_lost_InputDir as InputDir
from setting_param import MakeSample_repeat2_node_prediction_lost_utilize_existing_attribute_OutputDir as OutputDir_0
from setting_param import MakeSample_repeat2_node_prediction_lost_utilize_lost_OutputDir as OutputDir_1
from setting_param import MakeSample_repeat2_node_prediction_lost_utilize_new_attribute_link_OutputDir as OutputDir_2
from setting_param import MakeSample_repeat2_node_prediction_lost_utilize_disappeared_OutputDir as OutputDir_4
from setting_param import MakeSample_repeat2_node_prediction_lost_utilize_appeared_OutputDir as OutputDir_8
from setting_param import MakeSample_repeat2_node_prediction_lost_utilize_all_OutputDir as OutputDir_15
OutputDir = {0:OutputDir_0, 1:OutputDir_1, 2:OutputDir_2, 4:OutputDir_4, 8:OutputDir_8, 15:OutputDir_15}

from setting_param import L
from setting_param import attribute_dim
from setting_param import all_node_num
from setting_param import n_expanded

from repeat2_utils.graph_prediction import link_prediction
from setting_param import best_methods2 as best_methods
from setting_param import best_methods_attribute_new_OutputDir2 as best_methods_attribute_new_OutputDir
from repeat2_utils.get_predicted_new_attribute import get_predicted_new_attribute

for c_idx, Dir in OutputDir.items():
    os.makedirs(Dir, exist_ok=True)
    os.makedirs(Dir + "/input/", exist_ok=True)
    os.makedirs(Dir + "/input/node_attribute/", exist_ok=True)
    os.makedirs(Dir + "/input/adjacency", exist_ok=True)
    os.makedirs(Dir + "/label/", exist_ok=True)
    os.makedirs(Dir + "/mask/", exist_ok=True)

# READ EXIST_TABLE
EXIST_TABLE = np.load(InputDir + '/exist_table.npy')

n_node = EXIST_TABLE.shape[0]

def ExistNodeList(ts):
    assert ts >= 0, "ts < 0 [referrence error]"
    return np.where(EXIST_TABLE[:, ts]==1)[0]

def GetAppearedNodes(ts):
    return set(ExistNodeList(ts)) - set(ExistNodeList(ts-1))

def GetObservedNodes(ts, L):
    U = set()
    for i in range(L):
        U |= set(ExistNodeList(ts-i))
    return U

def GetNodes(ts, L, node_type):
    if node_type=='all':
        node_set = set(ExistNodeList(ts))
    elif node_type=='stay':
        node_set = set(ExistNodeList(ts-1)) & set(ExistNodeList(ts))
    elif node_type=='lost':
        node_set = set(ExistNodeList(ts-1)) - set(ExistNodeList(ts))
    elif node_type=='return':
        node_set = GetAppearedNodes(ts) - (GetAppearedNodes(ts) - GetObservedNodes(ts-1, L))
    elif node_type=='new':
        node_set = GetAppearedNodes(ts) - GetObservedNodes(ts-1, L)
        node_set |= GetNodes(ts, L, 'return')
    return node_set

def Nx(ts):
    return  nx.from_numpy_matrix(mmread(InputDir + '/adjacency' + str(ts)).toarray())

def SubNxNew(ts, L):
    return nx.Graph(Nx(ts).edges(GetNodes(ts, L, 'new')))

def SubNxLost(ts, L):
    return nx.Graph(Nx(ts-1).edges(GetNodes(ts, L, 'lost')))

def GetEdges(ts, L, edge_type):
    G_1 = Nx(ts)
    if edge_type == "all":
        edge_set = G_1.edges
    elif edge_type == 'stay':
        G_0 = Nx(ts - 1)
        edge_set = G_0.edges & G_1.edges
    elif edge_type == "appeared":
        G_0 = Nx(ts - 1)
        edge_set = G_1.edges - G_0.edges - SubNxNew(ts, L).edges
    elif edge_type == "disappeared":
        G_0 = Nx(ts - 1)
        edge_set = G_0.edges - G_1.edges - SubNxLost(ts, L).edges
    return edge_set

def get_adjacency_matrix(ts, L, edge_type):
    G = nx.Graph(list(GetEdges(ts, L, edge_type)))
    A = np.array(nx.to_numpy_matrix(G, nodelist=[i for i in range(n_node)]))
    return A

def get_exist_matrix(ts):
    index = np.where(EXIST_TABLE[:, ts] == 1)[0]
    exist_row = np.zeros((n_node, n_node))
    exist_row[index] = 1
    exist_col = np.zeros((n_node, n_node))
    exist_col[:, index] = 1
    return exist_row * exist_col

def NodeAttribute(ts):
    return  mmread(InputDir + '/node_attribute' + str(ts)).toarray()

def TsSplit(ts, L):
    ts_train = [(ts+l) for l in range(L)]
    ts_test = ts_train[-1]+1
    ts_all = ts_train.copy()
    ts_all.extend([ts_test])
    return ts_train, ts_test, ts_all

def concat_train_valid_test(train_result, valid_result, test_result):
    result = []
    for train_r in train_result:
        result.append(train_r)
    for valid_r in valid_result:
        result.append(valid_r)
    for test_r in test_result:
        result.append(test_r)
    ts_result_dic = {}
    for t_idx, ts in enumerate(range(L, EXIST_TABLE.shape[1]-L)):
        ts_result_dic[ts] = result[t_idx]
    return ts_result_dic

# リンク予測の結果をそれぞれbest_methodのOutputDirから取得
train_result = link_prediction(best_methods["n_appeared"], best_methods["p_appeared"], best_methods["n_disappeared"], best_methods["p_disappeared"], best_methods["n_new"], best_methods["p_new"], best_methods["n_lost"],  best_methods["p_lost"], True, False, False)
valid_result = link_prediction(best_methods["n_appeared"], best_methods["p_appeared"], best_methods["n_disappeared"], best_methods["p_disappeared"], best_methods["n_new"], best_methods["p_new"], best_methods["n_lost"],  best_methods["p_lost"], False, True, False)
test_result = link_prediction(best_methods["n_appeared"], best_methods["p_appeared"], best_methods["n_disappeared"], best_methods["p_disappeared"], best_methods["n_new"], best_methods["p_new"], best_methods["n_lost"],  best_methods["p_lost"], False, False, True)
pred_adjacency_matrix = concat_train_valid_test(train_result, valid_result, test_result)

# new nodeのattributeの結果をそれぞれbest_methodのOutputDirから取得
train_new = get_predicted_new_attribute(best_methods_attribute_new_OutputDir, True, False, False)
valid_new = get_predicted_new_attribute(best_methods_attribute_new_OutputDir, False, True, False)
test_new = get_predicted_new_attribute(best_methods_attribute_new_OutputDir, False, False, True)
pred_new_attribute_new = concat_train_valid_test(train_new, valid_new, test_new)

pred_attribute = {}
for c_idx in range(16):
    if not c_idx in [0, 1, 2, 4, 8, 15]:
        # 0 (既知ノード属性予測のみ), 1 (lost予測のみ), 2 (new(属性＋リンク)予測のみ), 4 (disappeared予測のみ), 8 (appeared予測のみ), 15 (全部) だけ実験する
        continue
    pred_attribute[c_idx] = {}
    for ts in range(L, EXIST_TABLE.shape[1]-L):
        ts_train, ts_test, ts_all = TsSplit(ts, L)
        # existing nodeのattribute と new nodeのattribute を concatする
        # existing nodeのattributeの結果を取得 (変化しないので直前のものを持って来る)
        pred_attribute_e = NodeAttribute(ts_train[-1])
        # new node のattributeの結果を取得
        pred_attribute_n = pred_new_attribute_new[ts]
        if c_idx == 0:
            pred_attribute[c_idx][ts] = pred_attribute_e
        elif c_idx == 1:
            alive_nodes = set(np.unique(np.where(pred_adjacency_matrix[ts][c_idx] > 0)).tolist())
            lost_node_list = sorted(set(GetNodes(ts_train[-1], L, 'all')) - alive_nodes)
            pred_attribute_e[lost_node_list, :] = pred_attribute_e[lost_node_list, :] * 0
            pred_attribute[c_idx][ts] = pred_attribute_e
        elif c_idx == 2:
            pred_attribute[c_idx][ts] = np.concatenate([NodeAttribute(ts_train[-1]), pred_attribute_n], axis=0)
        elif (c_idx == 4) or (c_idx == 8):
            pred_attribute[c_idx][ts] = NodeAttribute(ts_train[-1])
        elif c_idx == 15:
            alive_nodes = set(np.unique(np.where(pred_adjacency_matrix[ts][c_idx] > 0)).tolist())
            lost_node_list = sorted(set(GetNodes(ts_train[-1], L, 'all')) - alive_nodes)
            pred_attribute_e[lost_node_list, :] = pred_attribute_e[lost_node_list, :] * 0
            pred_attribute[c_idx][ts] = np.concatenate([pred_attribute_e, pred_attribute_n], axis=0)

for c_idx in range(16):
    if not c_idx in [0, 1, 2, 4, 8, 15]:
        # 0 (既知ノード属性予測のみ), 1 (lost予測のみ), 2 (new(属性＋リンク)予測のみ), 4 (disappeared予測のみ), 8 (appeared予測のみ) だけ実験する
        continue
    for ts in range(L, EXIST_TABLE.shape[1] - L):
        ts_train, ts_test, ts_all = TsSplit(ts, L)
        node_attribute = np.zeros((all_node_num + n_expanded, attribute_dim * L))
        npy_adjacency_matrix = np.zeros((all_node_num + n_expanded, (all_node_num + n_expanded) * L))

        # ノード属性, 隣接行列は t-L+2 から t までの観測値と t+1 の予測結果を使う
        for idx, ts_ in enumerate(ts_train[1:]):
            node_attribute[:all_node_num, attribute_dim * idx: attribute_dim * (idx + 1)] = NodeAttribute(ts_)
            npy_adjacency_matrix[:all_node_num,
            (all_node_num + n_expanded) * idx: (all_node_num + n_expanded) * idx + all_node_num] = get_adjacency_matrix(ts_, L, 'all')

        # ここでt+1の予測結果を加える
        node_attribute[:pred_attribute[c_idx][ts].shape[0], attribute_dim * (L - 1):] = pred_attribute[c_idx][ts]
        npy_adjacency_matrix[:, (all_node_num + n_expanded) * (L - 1):] = pred_adjacency_matrix[ts][c_idx]

        lil_adjacency_matrix = lil_matrix(npy_adjacency_matrix)
        lil_node_attribute = lil_matrix(node_attribute)
        mmwrite(OutputDir[c_idx] + "/input/node_attribute/" + str(ts), lil_node_attribute)
        mmwrite(OutputDir[c_idx] + "/input/adjacency/" + str(ts), lil_adjacency_matrix)

        label = np.zeros((all_node_num + n_expanded, 1))
        label[sorted(GetNodes(ts_test, L, 'lost')), 0] = 1
        mmwrite(OutputDir[c_idx] + "/label/" + str(ts), lil_matrix(label))

        mask = np.zeros((all_node_num + n_expanded, 1))
        mask[sorted(GetNodes(ts_train[-1], L, 'all')), 0] = 1
        mmwrite(OutputDir[c_idx] + "/mask/" + str(ts), lil_matrix(mask))
