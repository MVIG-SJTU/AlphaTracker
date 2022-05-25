
import os

checkFile = True
if not os.path.exists('./models/sppe/duc_se.pth'):
    print("Cannot find './models/sppe/duc_se.pth'")
    checkFile = False
if not os.path.exists('./train_yolo/darknet/darknet53.conv.74'):
    print("Cannot find './train_yolo/darknet/darknet53.conv.74'")
    checkFile = False
if not os.path.exists('./train_sppe/exp/coco/demo/model_10.pkl'):
    print("Cannot find './train_sppe/exp/coco/demo/model_10.pkl'")
    checkFile = False
if not os.path.exists('./train_yolo/darknet/backup/demo/yolov3-mice_final.weights'):
    print("Cannot find './train_yolo/darknet/backup/demo/yolov3-mice_final.weights'")
    checkFile = False
if not os.path.exists('./data/demo.mp4'):
    print("Cannot find './data/demo.mp4'")
    checkFile = False
if not os.path.exists('../../UI/data/scipy.data'):
    print("Cannot find '../../UI/data/scipy.data'")
    checkFile = False
if not os.path.exists('./data/sample_annotated_data/train9.json'):
    print("Cannot find './data/sample_annotated_data/train9.json'")
    checkFile = False
if not checkFile:
    download = False
    print("data are not downloaded properly.  Make sure that your computer network can reach google drive. You can also download these files manually following this link: https://github.com/ZexinChen/AlphaTracker/issues/9#issuecomment-1072844664")
