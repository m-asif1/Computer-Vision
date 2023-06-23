## Install & Load the resources

!pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl
#!pip install -q opencv-python
#!pip install -q pillow


!pip install tensorflow==1.15.3
#!pip install tensorflow==2.4.0

!pip install imageai --upgrade

from tensorflow.keras.models import load_model

import keras

import tensorflow as tf
import keras

print(tf.__version__, keras.__version__)

from imageai.Detection import VideoObjectDetection
import matplotlib as plt
import tensorflow as tf
import numpy as np
import scipy
import keras
import h5py

from tensorflow.python.keras.backend import get_session


## Create an instance of the Video ObjectDetection

detector = VideoObjectDetection()

# YOLO v3
# This function sets the model type of the object detection instance we created to the YOLOV3 model, 
# which means we will be performing our object detection tasks using the pre-trained "YOLOV3" model.

# We can also set the model either to RetinaNet with .setModelTypeAsRetinaNet() or to Tiny YOLOV3 with .setModelTypeAsTiny
YOLOV3()
detector.setModelTypeAsYOLOv3()

# Mount the drive to import yolo.h5 and the video
from google.colab import drive
drive.mount('/content/gdrive')

!ls '/content/gdrive/MyDrive/yolo'

# The model file
#This function accepts a string which must be the path to the model file we downloaded

!cd /content/gdrive/MyDrive/yolo

detector.setModelPath("/content/gdrive/MyDrive/yolo/yolo.h5")

## Load the model
from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()
detector.loadModel()

## Dectect Objects From Video
video_path = detector.detectObjectsFromVideo(input_file_path="/content/gdrive/MyDrive/yolo/traffic_video.mp4",
                                             output_file_path="/content/gdrive/MyDrive/yolo/video_output",
                                             frames_per_second=29, log_progress=True)