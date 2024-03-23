import cv2
import depthai as dai
import numpy as np

class define_pipeline:
    def __init__(self):
        self.pipeline = dai.Pipeline()
        
        stereo = self.createStereoNode()
        self.createLeftMonoCameraNode(self.pipeline, stereo)
        self.createRightMonoCameraNode(self.pipeline, stereo)
        self.createDisparityOutputNode(self.pipeline, stereo)
        self.createLeftCameraOutputNode(self.pipeline, stereo)
        self.createRightCameraOutputNode(self.pipeline, stereo)
        self.createDisparityMultiplier(stereo)

    def getPipeline(self):
        return self.pipeline

    def getDisparityMultiplier(self):
        return self.disparityMultiplier

    def createDisparityMultiplier(self, stereo):
        self.disparityMultiplier = 255 / stereo.initialConfig.getMaxDisparity()
        
    def createStereoNode(self):
        stereo = self.pipeline.createStereoDepth()
        stereo.setLeftRightCheck(True)
        return stereo

    def createLeftMonoCameraNode(self, pipeline, stereo):
        mono_left = pipeline.createMonoCamera()
        mono_left.setFps(40)
        mono_left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_480_P)
        mono_left.setBoardSocket(dai.CameraBoardSocket.CAM_B)
        mono_left.out.link(stereo.left)

    def createRightMonoCameraNode(self, pipeline, stereo):
        mono_right = pipeline.createMonoCamera()
        mono_right.setFps(40)
        mono_right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_480_P)
        mono_right.setBoardSocket(dai.CameraBoardSocket.CAM_C)
        mono_right.out.link(stereo.right)

    def createDisparityOutputNode(self, pipeline, stereo):
        xoutDisp = pipeline.createXLinkOut()
        xoutDisp.setStreamName("disparity")
        stereo.disparity.link(xoutDisp.input)

    def createLeftCameraOutputNode(self, pipeline, stereo):
        xoutRectifiedLeft = pipeline.createXLinkOut()
        xoutRectifiedLeft.setStreamName("RectifiedLeft")
        stereo.rectifiedLeft.link(xoutRectifiedLeft.input)

    def createRightCameraOutputNode(self, pipeline, stereo):
        xoutRectifiedRight = pipeline.createXLinkOut()
        xoutRectifiedRight.setStreamName("RectifiedRight")
        stereo.rectifiedRight.link(xoutRectifiedRight.input)

