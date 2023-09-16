import os

def isImageExtention(file):
    """Checks if a file is an image"""
    if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        return True
    return False


def getImageFilesInDir(path):
    """Returns a list of image files in a directory"""
    return [f for f in os.listdir(path) if isImageExtention(f)]

def getfiles(path, extenstion = None):
    """Returns a list of files in a directory"""
    if extenstion:
        return [f for f in os.listdir(path) if f.endswith(extenstion)]
    return os.listdir(path)