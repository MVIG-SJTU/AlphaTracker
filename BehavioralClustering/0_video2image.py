import numpy as np
import cv2
import json
import math
import copy

import os

from tqdm import tqdm
from contour_utils import mkdir_p

import setting


if __name__ == '__main__':
    arg = setting.args_class()
    
    for video_path, pose_track_vis_path,start_frame, end_frame in zip(arg.videodir,arg.imgdir,arg.start_frame,arg.end_frame):
        print('generating %s'%(video_path))
        cap = cv2.VideoCapture(video_path)
        if cap.isOpened():
            success = True
        else:
            success = False
            print(" read failed!make sure that the video format is supported by cv2.VideoCapture")

        if not os.path.exists(pose_track_vis_path):
            mkdir_p(pose_track_vis_path)

        for frame_index in tqdm(range(end_frame)):
            success, frame = cap.read()
            if not success:
                print('read frame failed!')
                break
            if frame_index < start_frame:
                continue
            cv2.imwrite(pose_track_vis_path + '/frame_{}.png'.format(frame_index), frame)
        
        cap.release()

    



