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