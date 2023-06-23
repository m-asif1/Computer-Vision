## **Object Detection**
---
Object detection, also called object localization, is the process of detecting objects and their bounding boxes in an image. A bounding box is the smallest rectangle of an image that fully contains an object.

A common input for an object detection algorithm is an image. A common output is a list of bounding boxes and object classes. For each bounding box, the model outputs the corresponding predicted class and its confidence.

## **YOLO: Algorithm for Object Detection**
Object detection is a popular task in computer vision. 

The core idea of YOLO is: **reframing object detection as a single regression problem**.

It deals with localizing a region of interest within an image and classifying this region like a typical image classifier. One image can include several regions of interest pointing to different objects. This makes object detection a more advanced problem of image classification.

YOLO (You Only Look Once) is a popular object detection model known for its speed and accuracy. It was first introduced by Joseph Redmon et al. in 2016 and has since undergone several iterations, the latest being YOLO v7.

## **Applications**
---
The applications of object detection are numerous and cover many industries. For instance,object detection can be used for the following purposes:   

- In self-driving cars, to locate other vehicles and pedestrians
- For content moderation, to locate forbidden objects and their respective size
- In health, to locate tumors or dangerous tissue using radiographs
- In manufacturing, for assembly robots to put together or repair products
- In the security industry, to detect threats or count people
- In wildlife conservation, to monitor an animal population

These are just a few examples—more and more applications are being discovered every day
as object localization becomes more powerful.

## **Video detection with Image Al and YOLO**
---
**Image Al** provided very powerful yet easy to use classes and functions to perform Video Object Detection and Tracking and
Video analysis.   
**ImageAl** allows you to perform all of these with state-of-the-art deep learning algorithms like RetinaNet, YOLOV3 and
TinyYOLOV3.    
With ImageAl you can run detection tasks and analyse videos and live-video feeds from device cameras and IP cameras.
In this tutorial we will implement a case study using YOLOV3 over a stored video. The code is inspired by the Image Al
documentation https://imageai.readthedocs.io/en/latest/detection/

1. Install & Load the resources
2. Create an instance of the Video ObjectDetection

3. YOLO v3
    - This function sets the model type of the object detection instance we created to the YOLOV3 model, which means we will be performing our object detection tasks using the pre-trained "YOLOV3" model.
    - We can also set the model either to RetinaNet with **.setModelTypeAsRetinaNet()** or to Tiny YOLOV3 with **.setModelTypeAsTiny
YOLOV3()**.
4. Mount the drive to import yolo.h5 and the video                 
5. The model file
    - path to the model file we downloaded

6. Load the model
    - function loads the model from the path we specified in the function call above into our object detection instance.
7. Dectect Objects From Video
    - function that performs object detecttion on a video file or video live-feed after the model has been loaded into the
instance we created.
---
**Check** [video input file view](https://drive.google.com/file/d/1H2M7xq3-9ZJUEOqEFhM-xR2YfZ4einJM/view?usp=sharing)
- parameter **input_file_path** (required if you did not set camera_input) : This refers to the path to the video file you want to
detect.    

**Check** [video Output file view](https://drive.google.com/file/d/1k-JT3oLJBV7vih2UdyRvKhAaQYvLpx6Y/view?usp=sharing)

- parameter **output_file_path** (required if you did not set save_detected_video = False): This refers to the path to which the
detected video will be saved. By default, this functionsaves video .avi format.
- parameter **frames per second** (optional, but recommended): This parameters allows you to set your desired frames per
second for the detected video that will be saved. The default value is 20 but we recommend you set the value that suits
your video or camera live-feed.
- parameter **log progress** (optional): Setting this parameter to True shows the progress of the video or live-feed as it is
detected in the CLI. It will report every frame detected as it progresses. The default value is False.
- parameter **camera_input** (optional) : This parameter can be set in replacement of the input_file_path if you want to detect
objects in the live-feed of a camera.