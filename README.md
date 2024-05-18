# oak-d_light_playground
The oak-d_light_playground repository on GitHub serves as an exploration hub for experimenting with the functionality of the oak-d camera.

## Usage
To execute the code in this repo, ensure the necessary libraries (`cv2` and `depthai`) are installed. You also need a Oak-d lite camera.

## hello_world

This code demonstrates how to capture and display frames from a monocular camera using the DepthAI library and OpenCV in Python. The DepthAI library facilitates complex computer vision pipelines and is particularly suited for depth perception tasks.

This code serves as a basic framework for capturing and displaying monocular camera feed. Additional functionalities such as image processing or depth estimation can be incorporated within the frame processing section.

## two_cameras

This builds on "hello_world" to display frames from both the left and the right cameras. The code also displays a third frame which combines the left and right frames, so you can clearly see the offset between the two images.

## depth_map

This code instead of just displaying the left and right cameras passes them both through the StereoDepth module first. This still allows us to display the “rectifiedLeft” and “rectifiedRight” images from the cameras. This StereoDepth module will also allow us to access the “disparity” or offset between the two images. The code uses this disparity to create a depth map showing the distance of the object in view.

## colour_camera

This code just displays the frames from the colour camera. 

## opencv_threshold

This Python code utilizes the OpenCV library and the DepthAI library to capture and process stereo images from an Oak-D camera. It defines a function getDisparityFrame() to generate a disparity map from the stereo images. The main() function sets up the pipeline for processing stereo images, retrieves frames from the camera, and displays various visualizations such as the left and right stereo images, the combined stereo image, and the disparity map. 

Additionally, it performs edge detection using the Canny algorithm on the left stereo image and applies thresholding on the disparity map. The program continuously loops until the user presses the 'q' key to exit, at which point it cleans up and terminates. This code is structured to execute the main() function when the script is run directly.

## Face Detection

This code employs the Haar cascade technique for face detection, utilizing an XML file downloaded from the official OpenCV repository: https://github.com/opencv/opencv/tree/master/data/haarcascades. Haar cascades are efficient classifiers used in object detection tasks, particularly well-suited for detecting faces in images or video streams. By leveraging machine learning algorithms, Haar cascades analyze features such as edges, lines, and textures to identify objects of interest within an image. This XML file contains pre-trained data necessary for the cascade classifier to recognize facial features accurately, enabling the code to detect faces reliably within the provided images or video frames.

## gen2-face-detection

This example was taken from https://github.com/luxonis/depthai-experiments/tree/master/gen2-face-detection/

## system_info

The provided Python code operates by creating a pipeline using the DepthAI library, which facilitates working with depth and AI processing tasks on specialized hardware. The pipeline consists of two main components: a system logger and an output link. The system logger periodically collects various system information, including DDR and CMX memory usage, heap memory usage for the Leon CSS and MSS subsystems, chip temperature readings, and CPU usage for both Leon CSS and MSS. This information is then streamed through the output link named "sysinfo." Upon execution, the code connects to the DepthAI device, starts the pipeline, and continuously retrieves system information from the output queue. The retrieved data is then passed to the printSystemInformation() function, which formats and prints the system information to the console. This code essentially provides real-time monitoring of critical system parameters, offering insights into the device's resource utilization and temperature, which can aid in performance optimization and troubleshooting.

## edge_detection

This Python code utilizes the DepthAI library to construct a processing pipeline for real-time edge detection from a color camera and a stereo camera setup. It first establishes nodes for cameras and edge detectors, then sets their properties such as resolution and filter kernels. The connections between nodes are defined, linking camera outputs to corresponding edge detector inputs. After connecting to the DepthAI device, the code enters a loop to continuously retrieve processed edge images and display them using OpenCV. Additionally, it allows interactive switching between different Sobel filter kernels by detecting user keystrokes, dynamically updating the edge detector configurations accordingly. This code provides a flexible and interactive framework for edge detection experimentation on DepthAI hardware.

## gen2-blur-faces

This code utilizes the DepthAI platform to perform real-time face detection and blurring in video streams. It sets up a pipeline with a color camera, a neural network for face detection, and an object tracker. The neural network is based on MobileNet and identifies faces in the camera feed with a confidence threshold. Detected faces are tracked, and a bounding box is created around each face. The bounding boxes are slightly expanded to ensure the entire face is covered. An elliptical mask is then applied to these regions, and a blurring effect is added using OpenCV. The result is a video stream where faces are blurred to protect privacy, while the rest of the frame remains unchanged. The processed video is displayed in real-time, and the application can be exited by pressing the 'q' key.

## my_fake

This code modifies a real-time face detection script using DepthAI to replace detected faces with a hand-drawn image instead of blurring them. The script sets up a DepthAI pipeline, integrating a color camera and a MobileNet-based neural network to detect faces. Detected faces are tracked, and their bounding boxes are slightly expanded to ensure they fully encompass the face. When a face is detected, its region in the video frame is replaced with a predefined hand-drawn image. This is achieved by resizing the replacement image to fit the bounding box of the detected face and overlaying it on the frame. The processed video, with the hand-drawn images replacing real faces, is displayed in real-time, and the application can be exited by pressing the 'q' key.