from PIL import Image

img=Image.open("sal.png")
#Transposing the image
t=img.transpose(Image.FLIP_LEFT_RIGHT) #Rotate the image left right
t.save("saveimg.png") #save the image
t.show()