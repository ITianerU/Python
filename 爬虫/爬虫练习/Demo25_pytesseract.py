import pytesseract as pt
from PIL import Image

image = Image.open('/home/itianeru/桌面/timg.jpeg')

text = pt.image_to_string(image)
print(text)