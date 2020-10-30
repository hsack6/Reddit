ROOT_PATH = "/Users/shohei/work/Reddit"
L = 3
ratio_test = 0.1
ratio_valid = 0.2

all_node_num = 8077
n_expanded = 1128 # (MakeSample/confirm_n_expanded.pyで確認できる)
adj_shape = (all_node_num, all_node_num * L)
max_nnz_am = 16834 # (Model/confirm_max_nnz_amで確認できる）隣接疎行列の全サンプルにおける非ゼロ要素数の最大値
attribute_dim = 300

######################################################################################################################
# ディレクトリ名の定義

# MakeSample IO dir
# prediction_num_of_edge
MakeSample_prediction_num_of_edge_InputDir = ROOT_PATH + "/data/graph"
MakeSample_prediction_num_of_edge_OutputDir = ROOT_PATH + "/data/learning_data/prediction_num_of_edge"
# prediction_num_of_node
MakeSample_prediction_num_of_node_InputDir = ROOT_PATH + "/data/graph"
MakeSample_prediction_num_of_node_OutputDir = ROOT_PATH + "/data/learning_data/prediction_num_of_node"
# link_prediction_appeared
MakeSample_link_prediction_appeared_InputDir = ROOT_PATH + "/data/graph"
MakeSample_link_prediction_appeared_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_appeared"
# link_prediction_disappeared
MakeSample_link_prediction_disappeared_InputDir = ROOT_PATH + "/data/graph"
MakeSample_link_prediction_disappeared_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_disappeared"
# node_prediction_lost
MakeSample_node_prediction_lost_InputDir = ROOT_PATH + "/data/graph"
MakeSample_node_prediction_lost_OutputDir = ROOT_PATH + "/data/learning_data/node_prediction_lost"
# attribute_prediction_new
MakeSample_attribute_prediction_new_InputDir = ROOT_PATH + "/data/graph"
MakeSample_attribute_prediction_new_OutputDir = ROOT_PATH + "/data/learning_data/attribute_prediction_new"
# attribute_prediction_new_PROSER
MakeSample_attribute_prediction_new_PROSER_InputDir = ROOT_PATH + "/data/graph"
MakeSample_attribute_prediction_new_PROSER_OutputDir = ROOT_PATH + "/data/learning_data/attribute_prediction_new_PROSER"


# link_prediction_new
MakeSample_link_prediction_new_InputDir = ROOT_PATH + "/data/graph"
MakeSample_link_prediction_new_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_new"
MakeSample_link_prediction_new_Baseline_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_new/Baseline"
MakeSample_link_prediction_new_DeepMatchMax_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_new/DeepMatchMax"
MakeSample_link_prediction_new_FNN_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_new/FNN"
# DynGEM embedding
MakeSample_link_prediction_appeared_DynGEM_InputDir = MakeSample_link_prediction_appeared_OutputDir
MakeSample_link_prediction_disappeared_DynGEM_InputDir = MakeSample_link_prediction_disappeared_OutputDir
MakeSample_node_prediction_lost_DynGEM_InputDir = MakeSample_node_prediction_lost_OutputDir
MakeSample_link_prediction_appeared_DynGEM_OutputDir = ROOT_PATH + "/data/learning_data/DynGEM_link_prediction_appeared"
MakeSample_link_prediction_disappeared_DynGEM_OutputDir = ROOT_PATH + "/data/learning_data/DynGEM_link_prediction_disappeared"
MakeSample_node_prediction_lost_DynGEM_OutputDir = ROOT_PATH + "/data/learning_data/DynGEM_node_prediction_lost"


# Model IO dir
# prediction_num_of_edge
# Baseline
Model_prediction_num_of_edge_InputDir = MakeSample_prediction_num_of_edge_OutputDir
Model_prediction_num_of_edge_new_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/new/Baseline"
Model_prediction_num_of_edge_appeared_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/appeared/Baseline"
Model_prediction_num_of_edge_disappeared_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/disappeared/Baseline"
# LSTM
Model_prediction_num_of_edge_InputDir = MakeSample_prediction_num_of_edge_OutputDir
Model_prediction_num_of_edge_new_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/new/LSTM"
Model_prediction_num_of_edge_appeared_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/appeared/LSTM"
Model_prediction_num_of_edge_disappeared_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/disappeared/LSTM"

# prediction_num_of_node
# Baseline
Model_prediction_num_of_node_InputDir = MakeSample_prediction_num_of_node_OutputDir
Model_prediction_num_of_node_new_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_node/new/Baseline"
Model_prediction_num_of_node_lost_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_node/lost/Baseline"
# LSTM
Model_prediction_num_of_node_InputDir = MakeSample_prediction_num_of_node_OutputDir
Model_prediction_num_of_node_new_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_node/new/LSTM"
Model_prediction_num_of_node_lost_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_node/lost/LSTM"

# link_prediction_appeared
Model_link_prediction_appeared_InputDir = MakeSample_link_prediction_appeared_OutputDir
Model_link_prediction_appeared_DynGEM_InputDir = MakeSample_link_prediction_appeared_DynGEM_OutputDir
Model_link_prediction_appeared_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/Baseline"
Model_link_prediction_appeared_Random_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/Random"
Model_link_prediction_appeared_COSSIMMLP_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/COSSIMMLP"
Model_link_prediction_appeared_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/STGGNN"
Model_link_prediction_appeared_EGCNh_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/EGCNh"
Model_link_prediction_appeared_STGCN_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/STGCN"
Model_link_prediction_appeared_EGCNo_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/EGCNo"
Model_link_prediction_appeared_GCN_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/GCN"
Model_link_prediction_appeared_DynGEM_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/DynGEM"
Model_link_prediction_appeared_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/LSTM"

# link_prediction_disappeared
Model_link_prediction_disappeared_InputDir = MakeSample_link_prediction_disappeared_OutputDir
Model_link_prediction_disappeared_DynGEM_InputDir = MakeSample_link_prediction_disappeared_DynGEM_OutputDir
Model_link_prediction_disappeared_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/Baseline"
Model_link_prediction_disappeared_Random_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/Random"
Model_link_prediction_disappeared_COSSIMMLP_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/COSSIMMLP"
Model_link_prediction_disappeared_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/STGGNN"
Model_link_prediction_disappeared_EGCNh_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/EGCNh"
Model_link_prediction_disappeared_STGCN_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/STGCN"
Model_link_prediction_disappeared_EGCNo_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/EGCNo"
Model_link_prediction_disappeared_GCN_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/GCN"
Model_link_prediction_disappeared_DynGEM_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/DynGEM"
Model_link_prediction_disappeared_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/LSTM"

# node_prediction_lost
Model_node_prediction_lost_InputDir = MakeSample_node_prediction_lost_OutputDir
Model_node_prediction_lost_DynGEM_InputDir = MakeSample_node_prediction_lost_DynGEM_OutputDir
Model_node_prediction_lost_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/Baseline"
Model_node_prediction_lost_Random_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/Random"
Model_node_prediction_lost_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/LSTM"
Model_node_prediction_lost_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/STGGNN"
Model_node_prediction_lost_EGCNh_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/EGCNh"
Model_node_prediction_lost_STGCN_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/STGCN"
Model_node_prediction_lost_EGCNo_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/EGCNo"
Model_node_prediction_lost_GCN_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/GCN"
Model_node_prediction_lost_DynGEM_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/DynGEM"
Model_node_prediction_lost_FNN_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/FNN"

# attribute_prediction_new
Model_attribute_prediction_new_InputDir = MakeSample_attribute_prediction_new_OutputDir
Model_attribute_prediction_new_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_new/Baseline"
Model_attribute_prediction_new_FNN_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_new/FNN"
Model_attribute_prediction_new_DeepMatchMax_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_new/DeepMatchMax"

# attribute_prediction_new_PROSER_oracle
Model_attribute_prediction_new_PROSER_oracle_InputDir = ROOT_PATH + "/data/graph"
Model_attribute_prediction_new_PROSER_oracle_OutputDir = ROOT_PATH + "/data/result/attribute_prediction_new_PROSER_oracle"

# attribute_prediction_new_PROSER
Model_attribute_prediction_new_PROSER_InputDir = MakeSample_attribute_prediction_new_PROSER_OutputDir
Model_attribute_prediction_new_PROSER_FNN_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_new_PROSER/FNN"

# link_prediction_new
Model_link_prediction_new_Baseline_mix_InputDir = MakeSample_link_prediction_new_Baseline_OutputDir + "/mix"
Model_link_prediction_new_Baseline_learning_InputDir = MakeSample_link_prediction_new_Baseline_OutputDir + "/learning"
Model_link_prediction_new_Baseline_inference_InputDir = MakeSample_link_prediction_new_Baseline_OutputDir + "/inference"

Model_link_prediction_new_DeepMatchMax_mix_InputDir = MakeSample_link_prediction_new_DeepMatchMax_OutputDir + "/mix"
Model_link_prediction_new_DeepMatchMax_learning_InputDir = MakeSample_link_prediction_new_DeepMatchMax_OutputDir + "/learning"
Model_link_prediction_new_DeepMatchMax_inference_InputDir = MakeSample_link_prediction_new_DeepMatchMax_OutputDir + "/inference"

Model_link_prediction_new_FNN_mix_InputDir = MakeSample_link_prediction_new_FNN_OutputDir + "/mix"
Model_link_prediction_new_FNN_learning_InputDir = MakeSample_link_prediction_new_FNN_OutputDir + "/learning"
Model_link_prediction_new_FNN_inference_InputDir = MakeSample_link_prediction_new_FNN_OutputDir + "/inference"

Model_link_prediction_new_COSSIMMLP_Baseline_mix_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/Baseline/mix"
Model_link_prediction_new_COSSIMMLP_Baseline_learning_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/Baseline/learning"
Model_link_prediction_new_COSSIMMLP_Baseline_inference_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/Baseline/inference"

Model_link_prediction_new_COSSIMMLP_DeepMatchMax_mix_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/DeepMatchMax/mix"
Model_link_prediction_new_COSSIMMLP_DeepMatchMax_learning_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/DeepMatchMax/learning"
Model_link_prediction_new_COSSIMMLP_DeepMatchMax_inference_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/DeepMatchMax/inference"

Model_link_prediction_new_COSSIMMLP_FNN_mix_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/FNN/mix"
Model_link_prediction_new_COSSIMMLP_FNN_learning_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/FNN/learning"
Model_link_prediction_new_COSSIMMLP_FNN_inference_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/FNN/inference"


# Evaluation IO dir
# prediction_num_of_edge
# Baseline
Evaluation_prediction_num_of_edge_new_Baseline_InputDir = Model_prediction_num_of_edge_new_Baseline_OutputDir
Evaluation_prediction_num_of_edge_appeared_Baseline_InputDir = Model_prediction_num_of_edge_appeared_Baseline_OutputDir
Evaluation_prediction_num_of_edge_disappeared_Baseline_InputDir = Model_prediction_num_of_edge_disappeared_Baseline_OutputDir
# LSTM
Evaluation_prediction_num_of_edge_new_LSTM_InputDir = Model_prediction_num_of_edge_new_LSTM_OutputDir
Evaluation_prediction_num_of_edge_appeared_LSTM_InputDir = Model_prediction_num_of_edge_appeared_LSTM_OutputDir
Evaluation_prediction_num_of_edge_disappeared_LSTM_InputDir = Model_prediction_num_of_edge_disappeared_LSTM_OutputDir
Evaluation_prediction_num_of_edge_new_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_edge/new"
Evaluation_prediction_num_of_edge_appeared_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_edge/appeared"
Evaluation_prediction_num_of_edge_disappeared_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_edge/disappeared"

# prediction_num_of_node
# Baseline
Evaluation_prediction_num_of_node_new_Baseline_InputDir = Model_prediction_num_of_node_new_Baseline_OutputDir
Evaluation_prediction_num_of_node_lost_Baseline_InputDir = Model_prediction_num_of_node_lost_Baseline_OutputDir
# LSTM
Evaluation_prediction_num_of_node_new_LSTM_InputDir = Model_prediction_num_of_node_new_LSTM_OutputDir
Evaluation_prediction_num_of_node_lost_LSTM_InputDir = Model_prediction_num_of_node_lost_LSTM_OutputDir
Evaluation_prediction_num_of_node_new_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_node/new"
Evaluation_prediction_num_of_node_lost_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_node/lost"

# link_prediction_appeared
Evaluation_link_prediction_appeared_Baseline_InputDir = Model_link_prediction_appeared_Baseline_OutputDir
Evaluation_link_prediction_appeared_Random_InputDir = Model_link_prediction_appeared_Random_OutputDir
Evaluation_link_prediction_appeared_COSSIMMLP_InputDir = Model_link_prediction_appeared_COSSIMMLP_OutputDir
Evaluation_link_prediction_appeared_STGGNN_InputDir = Model_link_prediction_appeared_STGGNN_OutputDir
Evaluation_link_prediction_appeared_EGCNh_InputDir = Model_link_prediction_appeared_EGCNh_OutputDir
Evaluation_link_prediction_appeared_STGCN_InputDir = Model_link_prediction_appeared_STGCN_OutputDir
Evaluation_link_prediction_appeared_EGCNo_InputDir = Model_link_prediction_appeared_EGCNo_OutputDir
Evaluation_link_prediction_appeared_GCN_InputDir = Model_link_prediction_appeared_GCN_OutputDir
Evaluation_link_prediction_appeared_DynGEM_InputDir = Model_link_prediction_appeared_DynGEM_OutputDir
Evaluation_link_prediction_appeared_LSTM_InputDir = Model_link_prediction_appeared_LSTM_OutputDir
Evaluation_link_prediction_appeared_OutputDir = ROOT_PATH + "/data/result/link_prediction_appeared"

# link_prediction_disappeared
Evaluation_link_prediction_disappeared_Baseline_InputDir = Model_link_prediction_disappeared_Baseline_OutputDir
Evaluation_link_prediction_disappeared_Random_InputDir = Model_link_prediction_disappeared_Random_OutputDir
Evaluation_link_prediction_disappeared_COSSIMMLP_InputDir = Model_link_prediction_disappeared_COSSIMMLP_OutputDir
Evaluation_link_prediction_disappeared_STGGNN_InputDir = Model_link_prediction_disappeared_STGGNN_OutputDir
Evaluation_link_prediction_disappeared_EGCNh_InputDir = Model_link_prediction_disappeared_EGCNh_OutputDir
Evaluation_link_prediction_disappeared_STGCN_InputDir = Model_link_prediction_disappeared_STGCN_OutputDir
Evaluation_link_prediction_disappeared_EGCNo_InputDir = Model_link_prediction_disappeared_EGCNo_OutputDir
Evaluation_link_prediction_disappeared_GCN_InputDir = Model_link_prediction_disappeared_GCN_OutputDir
Evaluation_link_prediction_disappeared_DynGEM_InputDir = Model_link_prediction_disappeared_DynGEM_OutputDir
Evaluation_link_prediction_disappeared_LSTM_InputDir = Model_link_prediction_disappeared_LSTM_OutputDir
Evaluation_link_prediction_disappeared_OutputDir = ROOT_PATH + "/data/result/link_prediction_disappeared"

# node_prediction_lost
Evaluation_node_prediction_lost_Baseline_InputDir = Model_node_prediction_lost_Baseline_OutputDir
Evaluation_node_prediction_lost_Random_InputDir = Model_node_prediction_lost_Random_OutputDir
Evaluation_node_prediction_lost_LSTM_InputDir = Model_node_prediction_lost_LSTM_OutputDir
Evaluation_node_prediction_lost_STGGNN_InputDir = Model_node_prediction_lost_STGGNN_OutputDir
Evaluation_node_prediction_lost_EGCNh_InputDir = Model_node_prediction_lost_EGCNh_OutputDir
Evaluation_node_prediction_lost_STGCN_InputDir = Model_node_prediction_lost_STGCN_OutputDir
Evaluation_node_prediction_lost_EGCNo_InputDir = Model_node_prediction_lost_EGCNo_OutputDir
Evaluation_node_prediction_lost_GCN_InputDir = Model_node_prediction_lost_GCN_OutputDir
Evaluation_node_prediction_lost_DynGEM_InputDir = Model_node_prediction_lost_DynGEM_OutputDir
Evaluation_node_prediction_lost_FNN_InputDir = Model_node_prediction_lost_FNN_OutputDir
Evaluation_node_prediction_lost_OutputDir = ROOT_PATH + "/data/result/node_prediction_lost"

# attribute_prediction_new
Evaluation_attribute_prediction_new_Baseline_InputDir = Model_attribute_prediction_new_Baseline_OutputDir
Evaluation_attribute_prediction_new_FNN_InputDir = Model_attribute_prediction_new_FNN_OutputDir
Evaluation_attribute_prediction_new_DeepMatchMax_InputDir = Model_attribute_prediction_new_DeepMatchMax_OutputDir
Evaluation_attribute_prediction_new_OutputDir = ROOT_PATH + "/data/result/attribute_prediction_new"

# attribute_prediction_new_PROSER
Evaluation_attribute_prediction_new_PROSER_InputDir = ROOT_PATH + "/data/graph"
Evaluation_attribute_prediction_new_PROSER_OutputDir = ROOT_PATH + "/data/result/attribute_prediction_new_PROSER"

# link_prediction_new
Evaluation_link_prediction_new_COSSIMMLP_Baseline_mix_InputDir = Model_link_prediction_new_COSSIMMLP_Baseline_mix_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_Baseline_learning_InputDir = Model_link_prediction_new_COSSIMMLP_Baseline_learning_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_Baseline_inference_InputDir = Model_link_prediction_new_COSSIMMLP_Baseline_inference_OutputDir

Evaluation_link_prediction_new_COSSIMMLP_DeepMatchMax_mix_InputDir = Model_link_prediction_new_COSSIMMLP_DeepMatchMax_mix_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_DeepMatchMax_learning_InputDir = Model_link_prediction_new_COSSIMMLP_DeepMatchMax_learning_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_DeepMatchMax_inference_InputDir = Model_link_prediction_new_COSSIMMLP_DeepMatchMax_inference_OutputDir

Evaluation_link_prediction_new_COSSIMMLP_FNN_mix_InputDir = Model_link_prediction_new_COSSIMMLP_FNN_mix_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_FNN_learning_InputDir = Model_link_prediction_new_COSSIMMLP_FNN_learning_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_FNN_inference_InputDir = Model_link_prediction_new_COSSIMMLP_FNN_inference_OutputDir

Evaluation_link_prediction_new_OutputDir = ROOT_PATH + "/data/result/link_prediction_new"

# graph_prediction
Evaluation_graph_prediction_OutputDir = ROOT_PATH + "/data/result/graph_prediction"

######################################################################################################################
# モデルハイパラメータの定義

# prediction_num_of_edge
prediction_num_of_edge_worker = 2
prediction_num_of_edge_batchSize = 1
prediction_num_of_edge_state_dim = 1
prediction_num_of_edge_output_dim = 1
prediction_num_of_edge_init_L = L
prediction_num_of_edge_niter = 1000
prediction_num_of_edge_patience = 10
prediction_num_of_edge_lr = 0.01
prediction_num_of_edge_max_appeared = 1229
prediction_num_of_edge_min_appeared = 1020
prediction_num_of_edge_max_disappeared = 1238
prediction_num_of_edge_min_disappeared = 1000
prediction_num_of_edge_max_new = 1229
prediction_num_of_edge_min_new = 981

# prediction_num_of_node
prediction_num_of_node_worker = 2
prediction_num_of_node_batchSize = 1
prediction_num_of_node_state_dim = 1
prediction_num_of_node_output_dim = 1
prediction_num_of_node_init_L = L
prediction_num_of_node_niter = 1000
prediction_num_of_node_patience = 10
prediction_num_of_node_lr = 0.01
prediction_num_of_node_max_new = 1128
prediction_num_of_node_min_new = 921
prediction_num_of_node_max_lost = 1065
prediction_num_of_node_min_lost = 897

# link_prediction_appeared
link_prediction_appeared_worker = 2
link_prediction_appeared_batchSize = 1
link_prediction_appeared_state_dim = attribute_dim
link_prediction_appeared_annotation_dim = attribute_dim
link_prediction_appeared_output_dim = all_node_num
link_prediction_appeared_init_L = L
link_prediction_appeared_niter = 100
link_prediction_appeared_n_steps = 5
link_prediction_appeared_patience = 10
link_prediction_appeared_lr = 0.01
link_prediction_appeared_egcnh_parameters_feats_per_node = 100
link_prediction_appeared_egcnh_parameters_feats_per_node_min = 100
link_prediction_appeared_egcnh_parameters_feats_per_node_max = 256
link_prediction_appeared_egcnh_parameters_layer_1_feats = 100
link_prediction_appeared_egcnh_parameters_layer_1_feats_min = 10
link_prediction_appeared_egcnh_parameters_layer_1_feats_max = 200
link_prediction_appeared_egcnh_parameters_layer_2_feats = 20
link_prediction_appeared_egcnh_parameters_layer_2_feats_same_as_l1 = True
link_prediction_appeared_egcnh_parameters_k_top_grcu = 200
link_prediction_appeared_egcnh_parameters_num_layers = 2
link_prediction_appeared_egcnh_parameters_lstm_l1_layers = 1
link_prediction_appeared_egcnh_parameters_lstm_l1_feats = 100 # only used with sp_lstm_B_trainer
link_prediction_appeared_egcnh_parameters_lstm_l1_feats_min = 10
link_prediction_appeared_egcnh_parameters_lstm_l1_feats_max = 100
link_prediction_appeared_egcnh_parameters_lstm_l2_layers = 1 # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
link_prediction_appeared_egcnh_parameters_lstm_l2_feats = None # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
link_prediction_appeared_egcnh_parameters_lstm_l2_feats_same_as_l1 = True
link_prediction_appeared_egcnh_parameters_cls_feats = 100 # Hidden size of the classifier
link_prediction_appeared_egcnh_parameters_cls_feats_min = 100
link_prediction_appeared_egcnh_parameters_cls_feats_max = 512
link_prediction_appeared_egcno_parameters_feats_per_node = 100
link_prediction_appeared_egcno_parameters_feats_per_node_min = 100
link_prediction_appeared_egcno_parameters_feats_per_node_max = 256
link_prediction_appeared_egcno_parameters_layer_1_feats = 152
link_prediction_appeared_egcno_parameters_layer_1_feats_min = 10
link_prediction_appeared_egcno_parameters_layer_1_feats_max = 200
link_prediction_appeared_egcno_parameters_layer_2_feats = 20
link_prediction_appeared_egcno_parameters_layer_2_feats_same_as_l1 = True
link_prediction_appeared_egcno_parameters_k_top_grcu = 200
link_prediction_appeared_egcno_parameters_num_layers = 2
link_prediction_appeared_egcno_parameters_lstm_l1_layers = 1
link_prediction_appeared_egcno_parameters_lstm_l1_feats = 35 # only used with sp_lstm_B_trainer
link_prediction_appeared_egcno_parameters_lstm_l1_feats_min = 10
link_prediction_appeared_egcno_parameters_lstm_l1_feats_max = 100
link_prediction_appeared_egcno_parameters_lstm_l2_layers = 1 # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
link_prediction_appeared_egcno_parameters_lstm_l2_feats = None # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
link_prediction_appeared_egcno_parameters_lstm_l2_feats_same_as_l1 = True
link_prediction_appeared_egcno_parameters_cls_feats = 147 # Hidden size of the classifier
link_prediction_appeared_egcno_parameters_cls_feats_min = 100
link_prediction_appeared_egcno_parameters_cls_feats_max = 512


# link_prediction_disappeared
link_prediction_disappeared_worker = 2
link_prediction_disappeared_batchSize = 1
link_prediction_disappeared_state_dim = attribute_dim
link_prediction_disappeared_annotation_dim = attribute_dim
link_prediction_disappeared_output_dim = all_node_num
link_prediction_disappeared_init_L = L
link_prediction_disappeared_niter = 100
link_prediction_disappeared_n_steps = 5
link_prediction_disappeared_patience = 10
link_prediction_disappeared_lr = 0.01
link_prediction_disappeared_egcnh_parameters_feats_per_node = 100
link_prediction_disappeared_egcnh_parameters_feats_per_node_min = 100
link_prediction_disappeared_egcnh_parameters_feats_per_node_max = 256
link_prediction_disappeared_egcnh_parameters_layer_1_feats = 100
link_prediction_disappeared_egcnh_parameters_layer_1_feats_min = 10
link_prediction_disappeared_egcnh_parameters_layer_1_feats_max = 200
link_prediction_disappeared_egcnh_parameters_layer_2_feats = 20
link_prediction_disappeared_egcnh_parameters_layer_2_feats_same_as_l1 = True
link_prediction_disappeared_egcnh_parameters_k_top_grcu = 200
link_prediction_disappeared_egcnh_parameters_num_layers = 2
link_prediction_disappeared_egcnh_parameters_lstm_l1_layers = 1
link_prediction_disappeared_egcnh_parameters_lstm_l1_feats = 100 # only used with sp_lstm_B_trainer
link_prediction_disappeared_egcnh_parameters_lstm_l1_feats_min = 10
link_prediction_disappeared_egcnh_parameters_lstm_l1_feats_max = 100
link_prediction_disappeared_egcnh_parameters_lstm_l2_layers = 1 # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
link_prediction_disappeared_egcnh_parameters_lstm_l2_feats = None # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
link_prediction_disappeared_egcnh_parameters_lstm_l2_feats_same_as_l1 = True
link_prediction_disappeared_egcnh_parameters_cls_feats = 100 # Hidden size of the classifier
link_prediction_disappeared_egcnh_parameters_cls_feats_min = 100
link_prediction_disappeared_egcnh_parameters_cls_feats_max = 512
link_prediction_disappeared_egcno_parameters_feats_per_node = 100
link_prediction_disappeared_egcno_parameters_feats_per_node_min = 100
link_prediction_disappeared_egcno_parameters_feats_per_node_max = 256
link_prediction_disappeared_egcno_parameters_layer_1_feats = 152
link_prediction_disappeared_egcno_parameters_layer_1_feats_min = 10
link_prediction_disappeared_egcno_parameters_layer_1_feats_max = 200
link_prediction_disappeared_egcno_parameters_layer_2_feats = 20
link_prediction_disappeared_egcno_parameters_layer_2_feats_same_as_l1 = True
link_prediction_disappeared_egcno_parameters_k_top_grcu = 200
link_prediction_disappeared_egcno_parameters_num_layers = 2
link_prediction_disappeared_egcno_parameters_lstm_l1_layers = 1
link_prediction_disappeared_egcno_parameters_lstm_l1_feats = 35 # only used with sp_lstm_B_trainer
link_prediction_disappeared_egcno_parameters_lstm_l1_feats_min = 10
link_prediction_disappeared_egcno_parameters_lstm_l1_feats_max = 100
link_prediction_disappeared_egcno_parameters_lstm_l2_layers = 1 # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
link_prediction_disappeared_egcno_parameters_lstm_l2_feats = None # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
link_prediction_disappeared_egcno_parameters_lstm_l2_feats_same_as_l1 = True
link_prediction_disappeared_egcno_parameters_cls_feats = 147 # Hidden size of the classifier
link_prediction_disappeared_egcno_parameters_cls_feats_min = 100
link_prediction_disappeared_egcno_parameters_cls_feats_max = 512

# node_prediction_lost
node_prediction_lost_worker = 2
node_prediction_lost_batchSize = 1
node_prediction_lost_state_dim = attribute_dim
node_prediction_lost_annotation_dim = attribute_dim
node_prediction_lost_output_dim = 1
node_prediction_lost_init_L = L
node_prediction_lost_niter = 100
node_prediction_lost_n_steps = 5
node_prediction_lost_patience = 10
node_prediction_lost_lr = 0.01
node_prediction_lost_egcnh_parameters_feats_per_node = 100
node_prediction_lost_egcnh_parameters_feats_per_node_min = 100
node_prediction_lost_egcnh_parameters_feats_per_node_max = 256
node_prediction_lost_egcnh_parameters_layer_1_feats = 100
node_prediction_lost_egcnh_parameters_layer_1_feats_min = 10
node_prediction_lost_egcnh_parameters_layer_1_feats_max = 200
node_prediction_lost_egcnh_parameters_layer_2_feats = 20
node_prediction_lost_egcnh_parameters_layer_2_feats_same_as_l1 = True
node_prediction_lost_egcnh_parameters_k_top_grcu = 200
node_prediction_lost_egcnh_parameters_num_layers = 2
node_prediction_lost_egcnh_parameters_lstm_l1_layers = 1
node_prediction_lost_egcnh_parameters_lstm_l1_feats = 100 # only used with sp_lstm_B_trainer
node_prediction_lost_egcnh_parameters_lstm_l1_feats_min = 10
node_prediction_lost_egcnh_parameters_lstm_l1_feats_max = 100
node_prediction_lost_egcnh_parameters_lstm_l2_layers = 1 # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
node_prediction_lost_egcnh_parameters_lstm_l2_feats = None # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
node_prediction_lost_egcnh_parameters_lstm_l2_feats_same_as_l1 = True
node_prediction_lost_egcnh_parameters_cls_feats = 100 # Hidden size of the classifier
node_prediction_lost_egcnh_parameters_cls_feats_min = 100
node_prediction_lost_egcnh_parameters_cls_feats_max = 512
node_prediction_lost_egcno_parameters_feats_per_node = 100
node_prediction_lost_egcno_parameters_feats_per_node_min = 100
node_prediction_lost_egcno_parameters_feats_per_node_max = 256
node_prediction_lost_egcno_parameters_layer_1_feats = 152
node_prediction_lost_egcno_parameters_layer_1_feats_min = 10
node_prediction_lost_egcno_parameters_layer_1_feats_max = 200
node_prediction_lost_egcno_parameters_layer_2_feats = 20
node_prediction_lost_egcno_parameters_layer_2_feats_same_as_l1 = True
node_prediction_lost_egcno_parameters_k_top_grcu = 200
node_prediction_lost_egcno_parameters_num_layers = 2
node_prediction_lost_egcno_parameters_lstm_l1_layers = 1
node_prediction_lost_egcno_parameters_lstm_l1_feats = 35 # only used with sp_lstm_B_trainer
node_prediction_lost_egcno_parameters_lstm_l1_feats_min = 10
node_prediction_lost_egcno_parameters_lstm_l1_feats_max = 100
node_prediction_lost_egcno_parameters_lstm_l2_layers = 1 # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
node_prediction_lost_egcno_parameters_lstm_l2_feats = None # only used with both sp_lstm_A_trainer and sp_lstm_B_trainer
node_prediction_lost_egcno_parameters_lstm_l2_feats_same_as_l1 = True
node_prediction_lost_egcno_parameters_cls_feats = 147 # Hidden size of the classifier
node_prediction_lost_egcno_parameters_cls_feats_min = 100
node_prediction_lost_egcno_parameters_cls_feats_max = 512

# attribute_prediction_new
attribute_prediction_new_worker = 2
attribute_prediction_new_batchSize = 1
attribute_prediction_new_d0 = attribute_dim
attribute_prediction_new_d1 = 300
attribute_prediction_new_d2 = 512
attribute_prediction_new_d3 = 1024
attribute_prediction_new_d4 = 512
attribute_prediction_new_d5 = 512
attribute_prediction_new_d6 = 300
attribute_prediction_new_init_L = L
attribute_prediction_new_niter = 100
attribute_prediction_new_patience = 10
attribute_prediction_new_lr = 0.01

# attribute_prediction_new_PROSER
attribute_prediction_new_PROSER_worker = 2
attribute_prediction_new_PROSER_batchSize = 1
attribute_prediction_new_PROSER_state_dim = attribute_dim * 2
attribute_prediction_new_PROSER_output_dim = 1
attribute_prediction_new_PROSER_target_idx = 4 # idx of percentile (min, 25, 50, 75, max)
attribute_prediction_new_PROSER_threshold = 0.88514332408633 # threshold of max
attribute_prediction_new_PROSER_init_L = L
attribute_prediction_new_PROSER_niter = 1000
attribute_prediction_new_PROSER_patience = 10
attribute_prediction_new_PROSER_lr = 0.001

# link_prediction_new
link_prediction_new_worker = 2
link_prediction_new_batchSize = 2
link_prediction_new_state_dim = attribute_dim
link_prediction_new_annotation_dim = attribute_dim
link_prediction_new_output_dim = all_node_num + n_expanded
link_prediction_new_init_L = L
link_prediction_new_niter = 1
link_prediction_new_n_steps = 5
link_prediction_new_patience = 3
link_prediction_new_lr = 0.01