from PIL import Image, ImageColor

# import the image
image = Image.open('Cat.jpg')

# documentation
# https://pillow.readthedocs.io/en/stable/reference/Image.html?

# rotated the image
# 1 image_rotate = image.rotate(60, expand=True, fillcolor=(255, 0, 255))
image_rotate = image.rotate(60, expand=True, fillcolor=ImageColor.getcolor('red', 'RGB'))
# print(ImageColor.getcolor('red', 'RGB'))

# display the image
image_rotate.show()
