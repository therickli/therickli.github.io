from io import StringIO
from PIL import Image

for i in range(1, 4):

    imagefile = f"./photos/趵突泉{i}.jpg"
    im1 = Image.open(imagefile)
    im1.save(f"./photos/趵突泉{i}compressed.jpg", "JPEG", quality=10)

