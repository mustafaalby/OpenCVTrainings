import cv2
import numpy as np
import sys


def main():
    decider=sys.argv[1]
    
    if decider==1:
        img1= cv2.imread('testImage.jpg')
        img1=cv2.resize(img1,(300,300))
        img2=cv2.imread('im2.jpg')
        img2=cv2.resize(img2,(300,300))
        #total=im1+im2 
        #adding 2 images pixel values
        total=cv2.add(img1,img2)
        #adding 2 images pixel values
        weight=cv2.addWeighted(img1,0.7,img2,0.3,0)
        
        cv2.imshow('total',total)
        cv2.imshow('weight',weight)
        cv2.waitKey()
        cv2.destroyAllWindows()
    else:
        img1= cv2.imread('testImage.jpg')
        mg1=cv2.resize(img1,(300,300))
        img2=cv2.imread('im2.jpg')
        img2=cv2.resize(img2,(300,300))

        rows,column,channel=img2.shape        
        #get the row column and channel info
        roi=img1[0:rows,0:column]        
        #region of interest with image rows and columns

        img2Gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        #get the image with gray scale
        ret,masks=cv2.threshold(img2Gray,180,255,cv2.THRESH_BINARY_INV)
        #for the values above 180 thresholds, set these values to 250 , works as binary

        mask_inv=cv2.bitwise_not(masks)#operation for cv2 or xor nor etc.
        
        img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
        img2_fg=cv2.bitwise_and(img2,img2,mask=masks)

        dst=cv2.add(img1_bg,img2_fg)
        img1[0:rows,0:column]=dst
        
        cv2.imshow('roi',roi)
        cv2.imshow('res',img1)
        cv2.imshow('mask_inv',mask_inv)
        cv2.imshow('img1_bg',img1_bg)
        cv2.imshow('img2_fg',img2_fg)
        cv2.imshow('dst',dst)
        cv2.waitKey()
        cv2.destroyAllWindows()
main()