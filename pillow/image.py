from PIL import Image

image = Image.open('cat_200_300.jpg')

print(image.format)
print(image.size)
print(image.mode)

rect = 80, 20, 310, 360
image.crop(rect).show()