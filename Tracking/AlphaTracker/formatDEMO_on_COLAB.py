import os
import shutil
import json
import gdown
import formatCOLAB


def download_models():

    if os.path.exists(
        "/content/drive/My Drive/AlphaTracker/Tracking/AlphaTracker/model10.pkl"
    ):
        os.remove(
            "/content/drive/My Drive/AlphaTracker/Tracking/AlphaTracker/model10.pkl"
        )

    if os.path.exists(
        "/content/drive/My Drive/AlphaTracker/Tracking/AlphaTracker/yolov3-mice_final.weights"
    ):
        os.remove(
            "/content/drive/My Drive/AlphaTracker/Tracking/AlphaTracker/yolov3-mice_final.weights"
        )

    # you can add https://drive.google.com/file/d/ in front of the following file_id and download them manually through web browser.
    sppe_pretrain_weight = '1OPORTWB2cwd5YTVBX-NE8fsauZJWsrtW'
    yolo_pretrain_weight = '1g8uJjK7EOlqrUCmjZTtCegwnNsBig6zn'
    sppe_trained_weight = '1_BwtYySpX9uWDgdwqw0UEppyMYYv1gkJ'
    yolo_trained_weight = '13zXkuZ4dNm3ZOwstr1sSWKOOzJ19XZpN'

    url = 'https://drive.google.com/uc?id='+ sppe_pretrain_weight
    output = '/content/drive/My Drive/AlphaTracker/Tracking/AlphaTracker/duc_se.pth'
    gdown.download(url, output, quiet=False)

    url = 'https://drive.google.com/uc?id='+ yolo_pretrain_weight
    output = '/content/drive/My Drive/AlphaTracker/Tracking/AlphaTracker/darknet53.conv.74'
    gdown.download(url, output, quiet=False)

    url = 'https://drive.google.com/uc?id='+ sppe_trained_weight
    output = '/content/drive/My Drive/AlphaTracker/Tracking/AlphaTracker/model_10.pkl'
    gdown.download(url, output, quiet=False)

    url = 'https://drive.google.com/uc?id='+ yolo_trained_weight
    output = '/content/drive/My Drive/AlphaTracker/Tracking/AlphaTracker/yolov3-mice_final.weights'
    gdown.download(url, output, quiet=False)


def download_data():

    if os.path.exists("/content/drive/My Drive/data.zip"):
        os.remove("/content/drive/My Drive/data.zip")

    if os.path.exists("/content/drive/My Drive/demo_video.mp4"):
        os.remove("/content/drive/My Drive/demo_video.mp4")

    if os.path.exists("/content/drive/My Drive/TRAINING_DATA"):
        shutil.rmtree("/content/drive/My Drive/TRAINING_DATA")

    # you can add https://drive.google.com/file/d/ in front of the following file_id and download them manually through web browser.
    demo_data = '1N0JjazqW6JmBheLrn6RoDTSRXSPp1t4K'
    sample_training_data='15dR-vVCEsg2z7mEVzJOF9YDW6YioEU3N'
    
    url = 'https://drive.google.com/uc?id='+ demo_data
    output = '/content/drive/My Drive/demo_video.mp4'
    gdown.download(url, output, quiet=False)   

    url = 'https://drive.google.com/uc?id='+ sample_training_data
    output = '/content/drive/My Drive/data.zip'
    gdown.download(url, output, quiet=False)

    # The following command do an unzip operation. You can also unzip the files manually.
    path_to_zip = "/content/drive/My Drive/data.zip"
    save_dir = "/content/drive/My Drive"
    with zipfile.ZipFile(path_to_zip, "r") as zip_file_rep:
        zip_file_rep.extractall(save_dir)

    formatCOLAB.convert(
        ["/content/drive/My Drive/demo"],
        ["/content/drive/My Drive/demo/train9.json"],
        "jpg",
    )
    shutil.rmtree("/content/drive/My Drive/demo")


def make_settingPY():

    with open("setting.py", "w") as f:
        f.write("import os\n")
        f.write("gpu_id=0\n")
        f.write("AlphaTracker_root = '/gdrive/AlphaTracker/Tracking/AlphaTracker'\n")
        f.write("image_root_list=['/gdrive/TRAINING_DATA']\n")
        f.write("json_file_list=['/gdrive/TRAINING_DATA/ATjsonCOLAB.json']\n")
        f.write("num_mouse=[2]\n")
        f.write("num_pose=4\n")
        f.write("exp_name='DEMO'\n")
        f.write("pose_pair=[[0,1],[0,2],[0,3]]\n")
        f.write("train_val_split=0.90\n")
        f.write("image_suffix='jpg'\n")
        f.write("sppe_lr=1e-4\n")
        f.write("sppe_epoch=5\n")
        f.write("sppe_batchSize=10\n")
        f.write(
            "sppe_pretrain='/gdrive/AlphaTracker/Tracking/AlphaTracker/model10.pkl'\n"
        )
        f.write("yolo_lr=0.0005\n")
        f.write("yolo_iter=100\n")
        f.write("yolo_batchSize=4\n")
        f.write(
            "yolo_pretrain='/gdrive/AlphaTracker/Tracking/AlphaTracker/yolov3-mice_final.weights'\n"
        )

        f.write("video_full_path='/gdrive/demo_video.mp4'\n")

        f.write("start_frame=0\n")
        f.write("end_frame=1000\n")
        f.write("max_pid_id_setting=2\n")
        f.write("result_folder='/gdrive/result_folder'\n")
        f.write("remove_oriFrame=False\n")

        f.write("vis_track_result=1\n")
        f.write("weights = '0 6 0 0 0 0 '\n")
        f.write("match = 0\n")
