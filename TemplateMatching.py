import numpy as np
import cv2

def main():

    imgGRY=cv2.imread('testImage.jpg')
    imgBGR=cv2.cvtColor(imgGRY,cv2.COLOR_BGR2GRAY)

    template=cv2.imread('template.jpg')
    width,height=template.shape[::-1]

    res=cv2.matchTemplate(imgGRY,template,cv2.TM_CCOEFF_NORMED)
    threshold=0.9
    loc=np.where(res>=threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(imgBGR, pt,(pt[0]+width,pt[1]+height),(0,255,255),2)
    
    cv2.imshow('detected',imgBGR)

main()