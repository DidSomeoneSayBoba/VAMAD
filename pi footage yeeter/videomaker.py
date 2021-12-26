import picamera
import os
import subprocess
import time
import paramiko


for _ in range(50):
    if True:
        camera = picamera.PiCamera()
        os.system('sudo rm upload.mp4')
        os.system('sudo rm upload.h264')
        camera.resolution = (640, 480)
        camera.start_recording('upload.h264')
        camera.wait_recording(10)
        camera.stop_recording()
        os.system("MP4Box -add upload.h264 upload.mp4")
        os.system('scp -i kengpu.pem upload.mp4 ubuntu@vamad-gpu.tmsoftwareinc.com:/home/ubuntu/yolov4-deepsort-master')
        k = paramiko.RSAKey.from_private_key_file("kengpu.pem")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        ssh.connect(hostname="vamad-gpu.tmsoftwareinc.com", username="ubuntu", pkey=k)
        stdin, stdout, stderr = ssh.exec_command('cd yolov4-deepsort-master; python videoyoinker.py')
        print(stdout.read())
        ssh.close()
        camera.close()

        