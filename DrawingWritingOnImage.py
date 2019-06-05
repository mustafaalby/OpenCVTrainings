import cv2
import numpy as np

def main():
    img=cv2.imread('testImage.jpg',cv2.IMREAD_COLOR)
    cv2.line(img,(0,0),(120,90),(255,255,0),20)
    #draw a line(image, starting point, finish point, rgb color, line thickness)
    cv2.rectangle(img,(5,20),(200,200),(255,0,0),10)
    #draw rectangle(image, left up point)
    cv2.circle(img,(250,250),60,(0,0,255),-1)#-1 fills inside circle

    font=cv2.FONT_ITALIC
    cv2.putText(img,'DENEME',(0,300),font,4,(155,255,155),2)
    #img,place,font,font size,color,margin
    cv2.imshow('image',img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()