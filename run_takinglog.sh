#!/usr/bin/env bash
WORK_PATH=$(pwd)
USER=`whoami`
HOST=`hostname`


cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_all/DynGEM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_appeared_utilize_all/LSTM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Evaluation
CURRENT_DIR=`pwd`
EXEC="python repeat1_link_prediction_appeared_utilize_all.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/Baseline
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/COSSIMMLP
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/EGCNh
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/EGCNo
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/GCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/Random
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/STGCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/STGGNN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_link_prediction_disappeared_utilize_all/DynGEM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Evaluation
CURRENT_DIR=`pwd`
EXEC="python repeat1_link_prediction_disappeared_utilize_all.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="