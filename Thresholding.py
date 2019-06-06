import cv2

def main():
    img=cv2.imread('im2.jpg')
    img=cv2.resize(img,(400,400))
    img2Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval,threshold=cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV)
    retvalGray,thresholdGray=cv2.threshold(img2Gray,80,255,cv2.THRESH_BINARY_INV)

    gaus=cv2.adaptiveThreshold(img2Gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    retval2, otsu=cv2.threshold(img2Gray,122,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('original',img)
    cv2.imshow('threshold',threshold)
    cv2.imshow('grayScale',img2Gray)
    cv2.imshow('grayScaleThreshold',thresholdGray)
    cv2.imshow('GAUS',gaus)
    cv2.imshow('otsu',otsu)
    cv2.waitKey()
    cv2.destroyAllWindows()

main()