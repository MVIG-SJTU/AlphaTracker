import os
import numpy as np

# code path setting
AlphaTracker_root = "./"

with open('train.cfg', 'r') as f:
    dat = f.read()
    if not dat:
        print(f'error, train.cfg is empty')
    try:
        dict_state = eval(dat)
    except Exception as e:
        print(f'load train.cfg Exception: {e}')
    print(dict_state)

gpu_id = int(dict_state['gpu_id'])    # the id of gpu that will be used

# data related settings
image_root_list = [dict_state['image_root_list']]    # list of image folder paths to the RGB images for training
json_file_list = [dict_state['json_file_list']]    # list of paths to the json files that contain labels of the images for training
num_mouse = [int(dict_state['num_mouse'])]     # the number of mouse in the images in each image folder path
exp_name = dict_state['exp_name']   # the name of the experiment
num_pose = int(dict_state['num_pose'])    # number of the pose that is labeled, remember to change self.nJoints in train_sppe/src/utils/dataset/coco.py

pose_pair = np.array([[float(j) for j in i.split('-')] for i in dict_state['pose_pair'].split(',')])
print('pose pair is:',pose_pair)
train_val_split = float(dict_state['train_val_split'])    # ratio of data that used to train model, the rest will be used for validation
image_suffix = dict_state['image_suffix']    # suffix of the image, png or jpg


# training hyperparameter setting
# Protip: if your training does not give good enough tracking you can lower lr and increase epoch number
# but lowering the lr too much can be bad for tracking quality as well. 
sppe_lr = float(dict_state['sppe_lr'])
sppe_epoch = int(dict_state['sppe_epoch'])
sppe_pretrain = dict_state['sppe_pretrain']
sppe_batchSize = int(dict_state['sppe_batchSize'])
yolo_lr = float(dict_state['yolo_lr'])
yolo_iter = int(dict_state['yolo_iter'])  ## if use pretrained model please make sure yolo_iter to be large enough to guarantee finetune is done
yolo_pretrain = dict_state['yolo_pretrain'] # './train_yolo/darknet/darknet53.conv.74'
yolo_batchSize = int(dict_state['yolo_batchSize'])


with open('track.cfg', 'r') as f:
    dat = f.read()
    if not dat:
        print(f'error, track.cfg is empty')
    try:
        dict_state2 = eval(dat)
    except Exception as e:
        print(f'load track.cfg Exception: {e}')
    print(dict_state2)


# demo video setting
# note video_full_path is for track.py, video_paths is for track_batch.py
# video_full_path is the path to the video that will be tracked
video_full_path = dict_state2['video_full_path']
video_paths = [
  dict_state2['video_full_path'],
  ]   # make sure video names are different from each other
start_frame = int(dict_state2['start_frame'])   # id of the start frame of the video
end_frame = int(dict_state2['end_frame'])   # id of the last frame of the video
max_pid_id_setting = int(dict_state2['max_pid_id_setting'])    # number of mice in the video
result_folder = dict_state2['result_folder']   # path to the folder used to save the result
remove_oriFrame = int(dict_state2['remove_oriFrame'])   # whether to remove the original frame that generated from video
vis_track_result = int(dict_state2['vis_track_result'])

# weights and match are parameter of tracking algorithm
# following setting should work fine, no need to change
weights = dict_state2['weights']
match = int(dict_state2['match'])

exp_name_track = dict_state2['exp_name_track']

# the following code is for self-check and reformat
assert len(image_root_list) == len(
    json_file_list
), "the length of image_root_list and json_file_list should be the same"
for i in range(len(image_root_list)):
    image_root_list[i] = os.path.abspath(image_root_list[i])
    json_file_list[i] = os.path.abspath(json_file_list[i])

AlphaTracker_root = os.path.abspath(AlphaTracker_root)
result_folder = os.path.abspath(result_folder)
