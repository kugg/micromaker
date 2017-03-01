import base64
import urllib2

from PIL import Image
from io import BytesIO

def fetch(url):
    """Get image at url, return image data"""
    response = urllib2.urlopen(url)
    image = response.read()
    return image

def resize(image_data):
    """Get image_data return thumbnailed base64 encoded data."""
    size = (64, 64)
    inbuffer = BytesIO(image_data)
    image = Image.open(inbuffer)

    image.thumbnail(size, Image.ANTIALIAS)
    background = Image.new('RGBA', size, (255, 255, 255, 0))
    background.paste(
        image,
        (int((size[0] - image.size[0]) / 2), # X size.
         int((size[1] - image.size[1]) /2)) # Y size.
    )
    
    outbuffer = BytesIO()
    background.save(outbuffer, format="JPEG")
    b64 = base64.b64encode(outbuffer.getvalue())
    return b64
