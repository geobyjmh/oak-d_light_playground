import cv2
import depthai as dai

# Start defining a pipeline
pipeline = dai.Pipeline()

# Define a color camera node
cam_rgb = pipeline.createColorCamera()
cam_rgb.setPreviewSize(500, 500)
cam_rgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)

# Create output
xout_rgb = pipeline.createXLinkOut()
xout_rgb.setStreamName("rgb")

# Link nodes
cam_rgb.preview.link(xout_rgb.input)

# Start the pipeline
with dai.Device(pipeline) as device:
    # Output queue will be used to get the rgb frames from the output defined above
    q_rgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)

    while True:
        # Get the rgb frames from the output queue
        in_rgb = q_rgb.tryGet()
        if in_rgb is not None:
            # Convert the rgb frame to numpy array
            frame_rgb = in_rgb.getCvFrame()
            # Display the frame
            cv2.imshow("Color Camera", frame_rgb)

        # Exit if 'q' key is pressed
        if cv2.waitKey(1) == ord('q'):
            print('Key "q" pressed')
            cv2.destroyAllWindows()
            break

print('******* End of program ********')
