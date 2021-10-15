import numpy as np
from PIL import Image
width=200
height=100
array=np.zeros([height,width,3],dtype=np.uint8)
array[50:,:]=[255,128,0] #orange color
array[:50,:]=[0,0,255] #blue color
img=Image.fromarray(array)
img.save("test.png")