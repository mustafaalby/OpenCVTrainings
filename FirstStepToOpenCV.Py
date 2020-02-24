import cv2
import numpy
import matplotlib.pyplot as plt


def main():
    img = cv2.imread("testImage.jpg", cv2.IMREAD_GRAYSCALE)
    # Read the image, pass it with gray scale
    # you could use 0 instead of IMREAD_GRAYSCALE like;
    # img=cv2.imread("testImage.jpg",cv2.0)

    cv2.imshow('title', img)
    # show the image with window title called title
    cv2.waitKey(0)
    # prevents closing instanly
    cv2.destroyAllWindows()

    plt.imshow(img, cmap='gray', interpolation='bicubic')
    # interpolation makes image blurry with different attributes
    plt.plot([20, 200], [50, 450], 'c', linewidth=5)
    plt.show()

    cv2.imwrite('testOutput.jpg', img)
    # having an output image


main()
