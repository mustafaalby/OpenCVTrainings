import cv2
import numpy as np

def main():
    
    img=cv2.imread('testImage.jpg')
    img=cv2.resize(img,(400,300))
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #BGR'yi HSV'ye çevir
    ## HSV renk uzayında yeşil renk oranını(range) ayarla
    lowerGreen=np.array([50,50,50])
    higherGreen=np.array([180,255,150])
    #Görüntüde yeşil renge threshold uygula
    mask=cv2.inRange(hsv,lowerGreen,higherGreen)
    #orjinal görüntüye bitwise and uygula
    res=cv2.bitwise_and(img,img,mask=mask)


    kernel=np.ones((5,5),np.float32)/25# 20*20=400
    smooth=cv2.filter2D(res,-1,kernel)

    blur=cv2.GaussianBlur(res,(15,15),0)
    median=cv2.medianBlur(res,15)
    biletarel=cv2.bilateralFilter(res,15,75,75)

    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('biletarel',biletarel)
    cv2.imshow('smooth',smooth)
    cv2.imshow('img',img)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)    
    cv2.waitKey()
    cv2.destroyAllWindows()

main()