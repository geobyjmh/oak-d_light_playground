import cv2
import depthai as dai
import numpy as np
from define_oakd_pipeline_nodes import define_pipeline

def getDisparityFrame(img, k):
    frame_disparity = img.getCvFrame()
    frame_disparity = (frame_disparity * k).astype(np.uint8)
    frame_disparity = cv2.applyColorMap(frame_disparity, cv2.COLORMAP_JET)
    return frame_disparity

def main():
    dp = define_pipeline()
    pipeline = dp.getPipeline()

    # Pipeline defined, now the device connection
    with dai.Device(pipeline) as device:

        # Output queue will be used to get the frames from the output defined above
        queue_disparity = device.getOutputQueue(name="disparity", maxSize=1, blocking=False)
        queue_mono_left = device.getOutputQueue(name="RectifiedLeft", maxSize=1, blocking=False)
        queue_mono_right = device.getOutputQueue(name="RectifiedRight", maxSize=1, blocking=False)
        
        while True:
            in_disparity = queue_disparity.get()
            in_mono_left = queue_mono_left.get()
            in_mono_right = queue_mono_right.get()
            
            if in_mono_left is not None:
                # Handle mono_left frame (e.g., display it).

                frame_disparity = getDisparityFrame(in_disparity, dp.getDisparityMultiplier())
                cv2.imshow("disparity", frame_disparity)
                
                frame_left = in_mono_left.getCvFrame()
                cv2.imshow("left (cam_b)", frame_left)
                
                frame_right = in_mono_right.getCvFrame()
                cv2.imshow("right (cam_c)", frame_right)
                
                frame_left_right = np.uint8(frame_left/2 + frame_right/2)
                cv2.imshow("Both left and right", frame_left_right)
                
                canny_left = cv2.Canny(frame_left, 125,125)
                cv2.imshow("Canny", canny_left)

                haar_cascade = cv2.CascadeClassifier('Face Detection/haar_face.xml')
                faces_rect = haar_cascade.detectMultiScale(frame_left, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
                frame_left =cv2.cvtColor(frame_left,cv2.COLOR_GRAY2BGR)
                for (x, y, w, h) in faces_rect:
                    cv2.rectangle(frame_left, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame_left, "face",(x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                
                cv2.imshow('Face Detection', frame_left)
                
            if cv2.waitKey(1) == ord('q'):
                print('Key "q" pressed')
                cv2.destroyAllWindows()
                break

    print('******* End of program ********')

if __name__ == "__main__":
    main()

