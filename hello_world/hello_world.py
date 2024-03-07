import cv2
import depthai as dai

# Define pipeline
pipeline = dai.Pipeline()

# Define source - color camera
cam_rgb = pipeline.createMonoCamera()
#cam_rgb.setPreviewSize(1080, 720)
#cam_rgb.setInterleaved(False)
cam_rgb.setFps(40)
cam_rgb.setBoardSocket(dai.CameraBoardSocket.CAM_B)


# Create output
xout = pipeline.createXLinkOut()
xout.setStreamName("left")
cam_rgb.out.link(xout.input)

# Pipeline defined, now the device connection
with dai.Device(pipeline) as device:
    # Start pipeline
    device.startPipeline()

    # Output queue will be used to get the frames from the output defined above
    q_rgb = device.getOutputQueue(name="left", maxSize=4, blocking=False)

    while True:
        in_rgb = q_rgb.get()
        if in_rgb is not None:
            # Handle rgb frame (e.g., display it)
            frame = in_rgb.getCvFrame()
            # ... (image processing or display)
            cv2.imshow("preview", frame)

        if cv2.waitKey(1) == ord('q'):
            break
