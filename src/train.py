import os
from ultralytics import YOLO

# Model Path
model_path = r'models/yolov8n.pt'

# Check if the model exists.
if not os.path.isfile(model_path):
    raise Exception(f'Model not found at {model_path}')

# Get the absolute path to dataset.yaml
dataset_yaml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset.yaml')

# Load model
model = YOLO(model_path)

# Training
results = model.train(
   data=dataset_yaml_path,
   imgsz=640, # (640 is default)
   epochs=1, # number of passes through entire dataset (try to avoid over and underfitting) (default 50)
   batch=2, # number of samples to work through before updating internal model parameters (8 was default)
   name='yolov8n_custom_attempt' #pick a suitable name
)
