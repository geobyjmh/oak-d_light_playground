import cv2
import depthai as dai

# Define pipeline
pipeline = dai.Pipeline()

# Define source - mono camera
mono = pipeline.createMonoCamera()
mono.setFps(40)
mono.setResolution(dai.MonoCameraProperties.SensorResolution.THE_480_P)
mono.setBoardSocket(dai.CameraBoardSocket.CAM_B)

# Create output
xout = pipeline.createXLinkOut()
xout.setStreamName("left_camera")
mono.out.link(xout.input)

# Pipeline defined, now the device connection
with dai.Device(pipeline) as device:

    # Output queue will be used to get the frames from the output defined above
    queue_mono = device.getOutputQueue(name="left_camera", maxSize=4, blocking=False)

    while True:
        in_mono = queue_mono.get()
        if in_mono is not None:
            # Handle mono frame (e.g., display it)
            frame = in_mono.getCvFrame()
            # ... (image processing or display)
            cv2.imshow("preview", frame)

        if cv2.waitKey(1) == ord('q'):
            print('Key "q" pressed')
            cv2.destroyAllWindows()
            break

print('******* End of program ********')
