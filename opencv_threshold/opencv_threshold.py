import cv2
import depthai as dai
import numpy as np
from define_oakd_pipeline_nodes import define_pipeline

dp = define_pipeline()
pipeline = dp.getPipeline()

# Pipeline defined, now the device connection
with dai.Device(pipeline) as device:

    # Output queue will be used to get the frames from the output defined above
    queue_disparity = device.getOutputQueue(name="disparity", maxSize=1, blocking=False)
    queue_mono_left = device.getOutputQueue(name="RectifiedLeft", maxSize=1, blocking=False)
    queue_mono_right = device.getOutputQueue(name="RectifiedRight", maxSize=1, blocking=False)

    disparityMultiplier = dp.getDisparityMultiplier()
    
    while True:
        in_disparity = queue_disparity.get()
        in_mono_left = queue_mono_left.get()
        in_mono_right = queue_mono_right.get()
        
        if in_mono_left is not None:
            # Handle mono_left frame (e.g., display it).
            frame_disparity = in_disparity.getCvFrame()
            frame_disparity = (frame_disparity * disparityMultiplier).astype(np.uint8)
            frame_disparity = cv2.applyColorMap(frame_disparity, cv2.COLORMAP_JET)
            
            frame_left = in_mono_left.getCvFrame()
            frame_right = in_mono_right.getCvFrame()
            frame_left_right = np.uint8(frame_left/2 + frame_right/2)
            
            # ... (image processing or display)
            
            cv2.imshow("left (cam_b)", frame_left)
            cv2.imshow("right (cam_c)", frame_right)
            cv2.imshow("disparity", frame_disparity)
            cv2.imshow("Both left and right", frame_left_right) 

        if cv2.waitKey(1) == ord('q'):
            print('Key "q" pressed')
            cv2.destroyAllWindows()
            break

print('******* End of program ********')
