# DOMAIN = {'people': {}}

# print DOMAIN['people']

from PIL import Image
from StringIO import StringIO

img_path = r"C:\Users\tliu\Pictures\advs_Logo.bmp"

# im = Image.open(StringIO(data))


im = Image.open(img_path)
width, height = im.size

print width, height 

# # im.rotate(0).show()

# size = 128, 128
# imth = im.thumbnail(size, Image.ANTIALIAS)

# outfile = r'C:\Temp\outPut1.jpg'
# im.save(outfile + ".thumbnail", "JPEG")


# box = (4000, 4000, 8000, 8000)

# xim = im.crop(box)

# outfile = r'C:\Temp\outPut1.jpg'

# xim.save(outfile)
