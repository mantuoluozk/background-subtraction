import numpy as np
import cv2
path = "F:/test.mp4"
cap = cv2.VideoCapture(0)

fgbg = cv2.bgsegm.createBackgroundSubtractorCNT()
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
#fgbg = cv2.bgsegm.createBackgroundSubtractorGSOC()
#fgbg = cv2.bgsegm.createBackgroundSubtractorLSBP()
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while(1):
    ret,frame = cap.read()
    if ret:
        fgmask = fgbg.apply(frame)
        cv2.namedWindow('org',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('org',800,500)
        cv2.imshow('org',frame)
    else:
        break
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame',800,500)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    #esc键退出
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()