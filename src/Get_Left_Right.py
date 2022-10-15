import cv2
import numpy as np
import depthai as dai

def main():
    print("a")

    pipeline = dai.Pipeline()
    monoLeft = pipeline.create(dai.node.MonoCamera)
    monoRight = pipeline.create(dai.node.MonoCamera)
    xoutLeft = pipeline.create(dai.node.XLinkOut)
    xoutRight = pipeline.create(dai.node.XLinkOut)

    xoutLeft.setStreamName('left')
    xoutRight.setStreamName('right')

    monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
    monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_720_P)
    monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)
    monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_720_P)
    
    monoRight.out.link(xoutRight.input)
    monoLeft.out.link(xoutLeft.input)

    device = dai.Device()
    print("s")
    i =0
    with device:
        device.startPipeline(pipeline)
        qLeft = device.getOutputQueue(name="left", maxSize=4, blocking=False)
        qRight = device.getOutputQueue(name="right", maxSize=4, blocking=False)
        while True:
            inLeft = qLeft.get()
            inRight = qRight.get()
            cv2.imshow("left", inLeft.getCvFrame())
            left = inLeft.getCvFrame()

            cv2.imshow("right", inRight.getCvFrame())
            right = inRight.getCvFrame()


            if cv2.waitKey(1) == ord('s'):
                cv2.imwrite('/home/prachi/Desktop/OAK-D/depthai/left_image' + str(i) + '.png',inLeft.getCvFrame())
                cv2.imwrite('/home/prachi/Desktop/OAK-D/depthai/right_image' + str(i) + '.png',inRight.getCvFrame())
                i += 1
                
        
            if cv2.waitKey(1) == ord('q'):
                break

if __name__ == '__main__':
    print('b')
    main()
