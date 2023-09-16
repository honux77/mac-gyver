# Image Resizer using PIL

import os
from PIL import Image

def isImagePIL(file):
    """Checks if a file is an image using PIL"""
    try:
        file = Image.open(file)
        file.close()
        return True
    except IOError:
        return False
    

def resizeImage(file, width, height):
    """Resizes an image to the specified width and height"""
    if not isImagePIL(file):
        raise Exception('File is not an image')
    
    img = Image.open(file)
    img = img.resize((width, height), Image.BILINEAR)
    img.save(file)

def resizeImageKeepRatio(file, ratio):
    """Resizes an image to the specified ratio"""
    if not isImagePIL(file):
        raise Exception('File is not an image')
    
    img = Image.open(file)
    width, height = img.size
    img = img.resize((int(width * ratio), int(height * ratio)), Image.NEAREST)
    img.save(file)

def cropImage(file, width, height, center=True):
    if not isImagePIL(file):
        raise Exception('File is not an image')
    
    img = Image.open(file)

    if center:
        # crop the center of the image
        w, h = img.size
        img = img.crop((w/2 - width/2, h/2 - height/2, w/2 + width/2, h/2 + height/2))
    else:
        # crop the top left of the image
        img = img.crop((0, 0, width, height))
    img.save(file)

def changeImageFormat(file, newformat = 'png', keepOld = False):
    """Changes the format of an image"""

    oldExt = file.split('.')[-1]

    # check if the file is an image
    if not file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        raise Exception('File is not an image')
    
    # check if the new format is an image
    if not newformat.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        raise Exception('New format is not an image')
    
    # check both files are the same format
    if oldExt == newformat:
        raise Exception('Both files are the same format')

    img = Image.open(file)
    img.save(file.split('.')[0] + '.' + newformat)
    if not keepOld:
        os.remove(file)
    