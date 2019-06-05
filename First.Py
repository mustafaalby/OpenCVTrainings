#%%
import cv2
import numpy
import matplotlib.pyplot as plt
#%%
img=cv2.imread("testImage.jpg",cv2.IMREAD_GRAYSCALE)
#Read the image, pass it with gray scale
cv2.imshow('title', img)
#show the image with window title called title
cv2.waitKey(0)
#prevents closing instanly
cv2.destroyAllWindows()


#%%
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([20,200],[50,450],'c',linewidth=5)
plt.show()

#%%
cv2.imwrite('testOutput.jpg',img)
#having an output image
#%%