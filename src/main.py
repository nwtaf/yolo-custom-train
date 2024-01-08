from ultralytics import YOLO
import os

def main():
    command0 = "yolo task=detect mode=train model=yolov8s.pt data=data.yaml epochs=300 imgsz=640 plots=True save=True batch=8" # start training
    command1 = "yolo task=detect mode=train resume model=/content/drive/MyDrive/yolov8/runs/detect/train6/weights/last.pt data=/content/drive/MyDrive/yolov8/data.yaml imgsz=640" # resume training
    command2 = "yolo val model=path/to/best.pt data=data.yaml split=test" # check test accuracy
    os.system(command0)
    # os.system(command1)
    # os.system(command2)