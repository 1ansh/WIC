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
                print "hello"


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
                    qr = qrtools.QR()

                    # Our operations on the frame come here
                    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Display the resulting frame
                    cv2.imshow('frame',frame)
                    cv2.imwrite( "frame.png", frame );
                    qr.decode("frame.png")
                    print qr.data
                    qr.destroy;
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

