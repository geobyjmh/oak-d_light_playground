import cv2
import depthai as dai
import numpy as np

# Define pipeline
pipeline = dai.Pipeline()

# Define source - mono_left camera
mono_left = pipeline.createMonoCamera()
mono_left.setFps(40)
mono_left.setBoardSocket(dai.CameraBoardSocket.CAM_B)

mono_right = pipeline.createMonoCamera()
mono_right.setFps(40)
mono_right.setBoardSocket(dai.CameraBoardSocket.CAM_C)

# Create output
xout_left = pipeline.createXLinkOut()
xout_left.setStreamName("left_camera")
mono_left.out.link(xout_left.input)

xout_right = pipeline.createXLinkOut()
xout_right.setStreamName("right_camera")
mono_right.out.link(xout_right.input)

# Pipeline defined, now the device connection
with dai.Device(pipeline) as device:

    # Output queue will be used to get the frames from the output defined above
    queue_mono_left = device.getOutputQueue(name="left_camera", maxSize=1, blocking=False)
    queue_mono_right = device.getOutputQueue(name="right_camera", maxSize=1, blocking=False)

    while True:
        in_mono_left = queue_mono_left.get()
        in_mono_right = queue_mono_right.get()
        
        if in_mono_left is not None:
            # Handle mono_left frame (e.g., display it)
            frame_left = in_mono_left.getCvFrame()
            frame_right = in_mono_right.getCvFrame()
            frame_left_right = np.uint8(frame_left/2 + frame_right/2)
            
            # ... (image processing or display)
            cv2.imshow("left (cam_b)", frame_left)
            cv2.imshow("right (cam_c)", frame_right)
            cv2.imshow("Both left and right", frame_left_right) 
            

        if cv2.waitKey(1) == ord('q'):
            print('Key "q" pressed')
            cv2.destroyAllWindows()
            break

print('******* End of program ********')
