#!/usr/bin/env bash
WORK_PATH=$(pwd)

# まず、当フレームワークの入力型の属性付き時系列グラフを作成してdata/graph以下に保存する。setting_paramにROOT_PATH, L, ratio_test, ratio_valid, all_node_num, attribute_dimを記入する。
# 次に、1までを実行して統計量の最大値、最小値を確認してsetting_paramに記入する。
# 次に、2までを実行して統計量の予測値を保存する
# 次に、3までを実行してn_expandedを確認してsetting_paramに記入する
# 次に、4までを実行してmax_nnz_amを確認してsetting_paramに記入する
# (次に、5までを実行してattribute_prediction_newの予測結果を保存する（5で止めずに最後まで実行して良い）)
# (次に、6までを実行して残り全ての学習サンプルを生成する（6で止めずに最後まで実行して良い）)
# 最後まで実行し、モデルの学習と学習結果の評価を行う

#============================================= 0 =============================================
#cd $WORK_PATH/MakeSample
#python prediction_num_of_edge.py # 標準出力される最小値、最大値をsetting_paramに記入
#python prediction_num_of_node.py # 標準出力される最小値、最大値をsetting_paramに記入
#============================================= 1 =============================================
#cd $WORK_PATH/Model/prediction_num_of_edge/Baseline
#python main.py appeared
#python main.py disappeared
#python main.py new
#cd $WORK_PATH/Model/prediction_num_of_edge/LSTM
#python main.py appeared
#python main.py disappeared
#python main.py new
#cd $WORK_PATH/Model/prediction_num_of_node/Baseline
#python main.py new
#python main.py lost
#cd $WORK_PATH/Model/prediction_num_of_node/LSTM
#python main.py new
#python main.py lost
#cd $WORK_PATH/Evaluation
#python prediction_num_of_edge.py appeared
#python prediction_num_of_edge.py disappeared
#python prediction_num_of_edge.py new
#python prediction_num_of_node.py new
#python prediction_num_of_node.py lost
#============================================= 2 =============================================
#cd $WORK_PATH/MakeSample
#python confirm_n_expanded.py # 標準出力されるn_expandedをsetting_paramに記入
#============================================= 3 =============================================
#cd $WORK_PATH/MakeSample
#python link_prediction_appeared.py
#cd $WORK_PATH/Model/confirm_max_nnz_am/print_max_nnz_am/
#python main.py # 標準出力されるmax_nnz_amをsetting_paramに記入
#============================================= 4 =============================================
#cd $WORK_PATH/MakeSample
#python attribute_prediction_new.py
#cd $WORK_PATH/Model/attribute_prediction_new/Baseline
#python main.py
#cd $WORK_PATH/Model/attribute_prediction_new/FNN
#python main.py
#cd $WORK_PATH/Model/attribute_prediction_new/DeepMatchMax
#python main.py
#cd $WORK_PATH/Evaluation
#python attribute_prediction_new.py
#============================================= 5 =============================================
#cd $WORK_PATH/MakeSample
#python link_prediction_new.py
#python link_prediction_disappeared.py
#python node_prediction_lost.py
#cd $WORK_PATH/MakeSample/DynGEM
#python main.py
#============================================= 6 =============================================
# node_prediction_lost学習
#cd $WORK_PATH/Model/node_prediction_lost/Baseline
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/EGCNh
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/EGCNo
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/GCN
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/LSTM
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/Random
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/STGCN
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/STGGNN
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/DynGEM
#python main.py
#cd $WORK_PATH/Model/node_prediction_lost/FNN
#python main.py
#cd $WORK_PATH/Evaluation
#python node_prediction_lost.py

#link_prediction_new学習&評価
#cd $WORK_PATH/Model/link_prediction_new/COSSIMMLP
#python main.py Baseline mix
#python main.py Baseline learning
#python main.py Baseline inference
#python main.py FNN mix
#python main.py FNN learning
#python main.py FNN inference
#python main.py DeepMatchMax mix
#python main.py DeepMatchMax learning
#python main.py DeepMatchMax inference
#python main.py PROSER mix
#python main.py PROSER learning
#python main.py PROSER inference
#cd $WORK_PATH/Evaluation
#python link_prediction_new.py

#link_prediction_appearedの学習&評価
#cd $WORK_PATH/Model/link_prediction_appeared/Baseline
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/EGCNh
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/EGCNo
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/GCN
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/Random
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/STGCN
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/STGGNN
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/DynGEM
#python main.py
#cd $WORK_PATH/Model/link_prediction_appeared/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python link_prediction_appeared.py

#link_prediction_disappeared学習&評価
#cd $WORK_PATH/Model/link_prediction_disappeared/Baseline
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/EGCNh
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/EGCNo
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/GCN
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/Random
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/STGCN
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/STGGNN
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/DynGEM
#python main.py
#cd $WORK_PATH/Model/link_prediction_disappeared/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python link_prediction_disappeared.py

# repeat
#cd $WORK_PATH/MakeSample
#python repeat1_link_prediction_appeared.py
#python repeat1_link_prediction_disappeared.py
#python repeat1_node_prediction_lost.py
#cd $WORK_PATH/MakeSample/DynGEM_repeat1
#python utilize_existing_attribute.py
#python utilize_lost.py
#python utilize_new_attribute_link.py
#python utilize_appeared.py
#python utilize_disappeared.py

#cd $WORK_PATH/Model/confirm_max_nnz_am/print_max_nnz_am/
#python main.py # 標準出力されるmax_nnz_am_expandedをsetting_paramに記入

# repeat1_node_prediction_lost_utilize_existing_attribute学習
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/LSTM
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_existing_attribute/FNN
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_node_prediction_lost_utilize_existing_attribute.py

# repeat1_node_prediction_lost_utilize_new_attribute_link学習
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/LSTM
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_new_attribute_link/FNN
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_node_prediction_lost_utilize_new_attribute_link.py

# repeat1_node_prediction_lost_utilize_appeared学習
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/LSTM
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_appeared/FNN
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_node_prediction_lost_utilize_appeared.py

# repeat1_node_prediction_lost_utilize_disappeared学習
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/LSTM
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_node_prediction_lost_utilize_disappeared/FNN
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_node_prediction_lost_utilize_disappeared.py

#repeat1_link_prediction_appeared_utilize_disappearedの学習&評価
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_disappeared/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_link_prediction_appeared_utilize_disappeared.py

#repeat1_link_prediction_appeared_utilize_existing_attributeの学習&評価
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_existing_attribute/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_link_prediction_appeared_utilize_existing_attribute.py

#repeat1_link_prediction_appeared_utilize_lostの学習&評価
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_lost/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_link_prediction_appeared_utilize_lost.py

#repeat1_link_prediction_appeared_utilize_new_attribute_linkの学習&評価
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_new_attribute_link/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_link_prediction_appeared_utilize_new_attribute_link.py

#repeat1_link_prediction_disappeared_utilize_appearedの学習&評価
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_appeared/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_link_prediction_disappeared_utilize_appeared.py

#repeat1_link_prediction_disappeared_utilize_existing_attributeの学習&評価
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_existing_attribute/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_link_prediction_disappeared_utilize_existing_attribute.py

#repeat1_link_prediction_disappeared_utilize_lostの学習&評価
cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/Baseline
python main.py
cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/COSSIMMLP
python main.py
cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/EGCNh
python main.py
cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/EGCNo
python main.py
cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/GCN
python main.py
cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/Random
python main.py
cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/STGCN
python main.py
cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/STGGNN
python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_lost/LSTM
#python main.py
cd $WORK_PATH/Evaluation
python repeat1_link_prediction_disappeared_utilize_lost.py

#repeat1_link_prediction_disappeared_utilize_new_attribute_linkの学習&評価
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/Baseline
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/COSSIMMLP
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/EGCNh
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/EGCNo
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/GCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/Random
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/STGCN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/STGGNN
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/DynGEM
#python main.py
#cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_new_attribute_link/LSTM
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat1_link_prediction_disappeared_utilize_new_attribute_link.py