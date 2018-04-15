from threading import Thread
import numpy as np
import time
import cv2
import qrtools


class CamVideoStream:

        def __init__(self):
               
                # initialize the camera and stream
                self.cap = cv2.VideoCapture(0)
                self.stopped = False


        def start(self):
                # start the thread to read frames from the video stream
                Thread(target=self.update, args=()).start()
                print("USB Cam Thread starting")
                time.sleep(3);
                return self

        def update(self):
                while(True):
                    # Capture frame-by-frame
                    ret, frame = self.cap.read()
                    H , W , _ = frame.shape
                    roi_u = frame[1:240,:]
                    roi_l = frame[240:480,:]
                    qru = qrtools.QR()
                    
                    # Our operations on the frame come here
                    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Display the resulting frame
                    #cv2.imshow('frame',frame)
                    cv2.imwrite( "roi_u.png", roi_u);
                    qru.decode("roi_u.png")
                    if(qru.data!="NULL"):
                            print qru.data
                            print("upper")
                    qru.destroy;
                    qrl = qrtools.QR()
                    cv2.imwrite( "roi_l.png", roi_l);
                    qrl.decode("roi_l.png")
                    if(qrl.data!="NULL"):
                            print qrl.data
                            print("lower")
                    qrl.destroy;
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                                # if the thread indicator variable is set, stop the thread
                                # and resource camera resources
                    if self.stopped:
                        self.cap.release()
                        cv2.destroyAllWindows()
                return

        def stop(self):
                # indicate that the thread should be stopped
                self.stopped = True

print "hi"
x = CamVideoStream().start()

