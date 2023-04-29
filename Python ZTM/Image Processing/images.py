from PIL import Image, ImageFilter

# creates an object
img = Image.open('.vscode/Python ZTM/Image Processing/pikachu.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)

# filtered image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save(".vscode/Python ZTM/Image Processing/blur.png", "png")
filtered_img.show()

# greyscale image
grey_img = img.convert('L')
grey_img.save(".vscode/Python ZTM/Image Processing/grey.png", 'png')
grey_img.show()

# rotated image
rotated_img = img.rotate(90)
rotated_img.save(".vscode/Python ZTM/Image Processing/rotated.png", "png")
rotated_img.show()

# resized image
resized_img = img.resize((300, 300))
resized_img.save(".vscode/Python ZTM/Image Processing/resized.png", "png")
resized_img.show()

# cropped image
box = (100, 100, 400, 400)
cropped_img = img.crop(box)
cropped_img.save(".vscode/Python ZTM/Image Processing/cropped.png", "png")
cropped_img.show()
