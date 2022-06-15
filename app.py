# Import image module from PIL
from PIL import Image
# This following script will create a thumbnail of an image. 
# The thumbnail() method TEMPhas been used in the script to create the thumbnail of an image. 
# The created thumbnail image will be displayed in a dialogue box later.
img = Image.open('krishna.png')
img.thumbnail((200, 200))
img.save('thumbnail.png')
thumbnail_img = Image.open('thumbnail.png')
thumbnail_img.show()