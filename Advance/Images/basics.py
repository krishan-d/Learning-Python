"""
Working with Image with python
pip install pillow
documentation: pillow.readthedocs.io
"""

from PIL import Image

# opening images:
image_name = 'Fire.jpg'
with Image.open(image_name) as mac:
    print(mac)
    print(type(mac))
    # show(self, title=None): -> None: ...
    # Display this image
    # The image is first saved to a temporary file. By default, it will be in PNG format.
    # mac.show()
    print(mac.size)
    print(mac.format_description)

    # Cropping Image:
    # crop(self, box: _Box | None = ...) -> Image: ...
    x, y = 700 // 4, 1050 // 4
    w, h = 700 // 2, 1050 // 2
    cropped_image = mac.crop((x, y, w, h))
    # cropped_image.show('Cropped')

    # resize(self, size, resample=None, box=None, reducing_gap=None) -> Image: ...
    resized_image = mac.resize((700, 1000))
    # resized_image.show()

    # def rotate(self,angle,resample=Resampling.NEAREST,expand=0,center=None,translate=None,fillcolor=None):-> Image: .
    mac = mac.rotate(90)
    # mac.show()


# Color Transparency: RGBA
image_name = 'colors.jpg'
img = Image.open(image_name)
# img.show()

# putalpha(self, alpha):
# Adds or replaces the alpha layer in this image.  If the image
# does not have an alpha layer, it's converted to "LA" or "RGBA".
# The new layer must be either "L" or "1".
img.putalpha(100)  # 0-255 | 0 means Transparent
# img.show()

# h = img.size[0]//2
h = 100
# paste(self, im: Image, box: tuple[float, float] | _Box | None = ..., mask: Image | None = ...) -> None: ...
# Pastes another image into this image.
img.paste(im=img, box=(h, 0), mask=img)
img.show()
img.save('rainbow.png')
img.close()
