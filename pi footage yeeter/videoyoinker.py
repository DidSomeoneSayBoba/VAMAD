import os
import time
print("normal model, 0.5")
#os.system("python object_tracker.py --weights ./checkpoints/yolov4-tiny-416 --model yolov4 --video upload.mp4 --tiny --score 0.1")
os.system("python object_tracker.py --model yolov4 --video upload.mp4 --score 0.5")
os.system("sudo rm /home/ubuntu/yolov4-deepsort-master/upload.mp4")
