import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np

img = plt.imread("test.jpg") 

plt.imshow(img)                                    
pylab.show()

#这个是设置的滤波，也就是卷积核
fil = np.array([[ -1,-1, 0],                        
                [ -1, 0, 1],
                [  0, 1, 1]])

res = cv2.filter2D(img,-1,fil)                      

plt.imshow(res)                                     
plt.imsave("res.jpg",res)
pylab.show()