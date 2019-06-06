#%%
import cv2
import numpy as np

def main():

    img=cv2.imread('testImage.jpg')
    img=cv2.resize(img,(400,300))
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerGreen=np.array([50,50,50])
    higherGreen=np.array([180,255,150])
    mask=cv2.inRange(hsv,lowerGreen,higherGreen)
    res=cv2.bitwise_and(img,img,mask=mask)
    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)
    #erosion gürültülü beyaz noktalarını silerek temizleme yapar
    #böylelikle beyaz noktalar ve nesne büyüklüğü azalalır

    #dilation siyah gürültü noktalarını silerek gürültüyü azaltır
    #beyaz noktalar ve nesne büyür

    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    #Opening is just another name of erosion followed by dilation.
    #beyaz alan dışındaki beyaz noktaları siler
    #Closing is reverse of Opening, Dilation followed by Erosion.
    #beyaz alan içindeki siyah noktaları siler
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)

    cv2.imshow('eresion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.waitKey()
    cv2.destroyAllWindows()


main()