#!/usr/bin/env bash
WORK_PATH=$(pwd)

# ここからrepeat3
cd $WORK_PATH/MakeSample
#python repeat3_link_prediction_appeared.py
python repeat3_link_prediction_disappeared.py
#python repeat3_node_prediction_lost.py
#python repeat3_attribute_prediction_new.py

#repeat3_link_prediction_appeared_utilize_allの学習&評価
#cd $WORK_PATH/Model/repeat3_link_prediction_appeared_utilize_all/STGGNN
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat3_link_prediction_appeared_utilize_all.py

#repeat3_link_prediction_disappeared_utilize_allの学習&評価
cd $WORK_PATH/Model/repeat3_link_prediction_disappeared_utilize_all/LSTM
python main.py
cd $WORK_PATH/Evaluation
python repeat3_link_prediction_disappeared_utilize_all.py

# repeat3_node_prediction_lost_utilize_all学習
cd $WORK_PATH/Model/repeat3_node_prediction_lost_utilize_all/STGCN
python main.py
cd $WORK_PATH/Evaluation
python repeat3_node_prediction_lost_utilize_all.py

# repeat3_attribute_prediction_new_utilize_new_attribute_link学習
#cd $WORK_PATH/Model/repeat3_attribute_prediction_new_utilize_new_attribute_link/FNN
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat3_attribute_prediction_new_utilize_new_attribute_link.py

#cd $WORK_PATH/MakeSample
#python repeat3_link_prediction_new_AGATE.py

#repeat3_link_prediction_new_AGATE
#cd $WORK_PATH/Model/repeat3_link_prediction_new_AGATE/DEAL
#python main.py
#cd $WORK_PATH/Evaluation
#python repeat3_link_prediction_new_AGATE.py