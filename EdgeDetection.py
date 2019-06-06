import numpy as np
import cv2


def main():


    img=cv2.imread('im2.jpg')
    
    laplacian=cv2.Laplacian(img,cv2.CV_64F)
    sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(img,100,100)
    cv2.imshow('edges',edges)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('img',img)
    cv2.imshow('laplacian',laplacian)
    cv2.waitKey()
    cv2.destroyAllWindows

main()