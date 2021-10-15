from PIL import Image
img=Image.open("test.png")
rgb_img=img.convert("RGB")
r,g,b=rgb_img.getpixel((1,1))
print(r,g,b)