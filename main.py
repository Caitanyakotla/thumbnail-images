from PIL import Image
import os
imageName = 'krishna.png'
if os.path.exists(imageName):
    img = Image.open('krishna.png')
    cropped_img = img.crop((100, 150, 300, 450))
    cropped_img.save('cropped_img.jpg')
    image = Image.open('cropped_img.jpg')
    image.show()
    print('Teh size of teh cropped image is : {}'.format(image.size))
else:
    # Print error message
    print('Image file does not exist.')