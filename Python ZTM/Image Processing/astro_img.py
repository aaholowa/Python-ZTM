from PIL import Image, ImageFilter

img = Image.open(".vscode/Python ZTM/Image Processing/robo.jpg")
print(img.size)

new_img = img.resize((694, 436))  # watch out for aspect ratio
new_img.save(".vscode/Python ZTM/Image Processing/astro4.jpg")

# thumbnail for proper proportions
new_img.thumbnail((694, 436))
new_img.save(".vscode/Python ZTM/Image Processing/arctos.jpg")
