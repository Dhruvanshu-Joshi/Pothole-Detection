import cv2
import numpy as np
import depthai as dai


pipeline = dai.Pipeline()

# Define sources and outputs
monoLeft = pipeline.create(dai.node.MonoCamera)
monoRight = pipeline.create(dai.node.MonoCamera)
xoutLeft = pipeline.create(dai.node.XLinkOut)
xoutRight = pipeline.create(dai.node.XLinkOut)

xoutLeft.setStreamName('left')
xoutRight.setStreamName('right')

# Properties
monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_720_P)
monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_720_P)

# Linking
monoRight.out.link(xoutRight.input)
monoLeft.out.link(xoutLeft.input)

device = dai.Device()
cams = device.getConnectedCameras()
depth_enabled = dai.CameraBoardSocket.LEFT in cams and dai.CameraBoardSocket.RIGHT in cams
if not depth_enabled:
    raise RuntimeError("Unable to run this experiment on device without left & right cameras! (Available cameras: {})".format(cams))
calibObj = device.readCalibration()

width = monoLeft.getResolutionWidth()
height = monoLeft.getResolutionHeight()

M_left = np.array(calibObj.getCameraIntrinsics(calibObj.getStereoLeftCameraId(), width, height))
M_right = np.array(calibObj.getCameraIntrinsics(calibObj.getStereoRightCameraId(), width, height))
R1 = np.array(calibObj.getStereoLeftRectificationRotation())
R2 = np.array(calibObj.getStereoRightRectificationRotation())

H_left = np.matmul(np.matmul(M_right, R1), np.linalg.inv(M_left))
H_right = np.matmul(np.matmul(M_right, R2), np.linalg.inv(M_right))

baseline = calibObj.getBaselineDistance() * 10 # mm
focalLength = M_right[0][0]

print(width)
print(height)
print(M_left)
print(M_right)
print(R1)
print(R2)
print(H_left )
print(H_right)
print(baseline)
print(focalLength)

#f = open("camerainfo.txt", "x")
#f.write(M_left + '/n' + M_right + '/n' + width + '/n' + height + '/n' + R1 + '/n' + R2 + '/n' + H_left + '/n' + H_right + '/n' + baseline + '/n' + focalLength)
#f.close()
