#!/usr/bin/env python
# coding: utf-8

# # #### Reading, writing and displaying images with OpenCV

# Let's start by importing the OpenCV libary 

# In[1]:


#import cv2 
import cv2


# In[2]:


# Now let's import numpy

import numpy as np 


# Let's now load our first image

# In[3]:



# Load an image using 'imread' specifying the path to image
input = cv2.imread('./image_examples/elephant.jpg')
print(input.shape)
# output:- (519, 778, 3)  The 2D dimensions are 830 pixels in high bv 1245 pixels wide. 
#The '3L' means that there are 3 other components (RGB) that make up this image.



# To display our image variable, use 'imshow' .

cv2.imshow('Test Elephant Image', input)

# 'waitKey' allows us to input information when a image window is open
# By leaving it blank it just waits for anykey to be pressed before 
# continuing. By placing numbers (except 0), we can specify a delay for
# how long you keep the window open (time is in milliseconds here)
cv2.waitKey()

# This closes all open windows 
cv2.destroyAllWindows()

# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('output.jpg', input)


# In[7]:





# 

# In[8]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




