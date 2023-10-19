import os
from os import path

def isImageExtention(file):
    """Checks if a file is an image"""
    if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        return True
    return False


def getImageFilesInDir(dirName):
    """Returns a list of image files in a directory"""
    return [f for f in os.listdir(dirName) if isImageExtention(f)]

def replaceBackslashWithForwardslash(filename):
    """Replaces backslash with forward slash"""
    return filename.replace('\\', '/')

def getfilesInDirectory(dirName, extenstions = []):
    """
    Returns a list of files in a directory
    if extenstion is specified, returns a list of files with the extenstion
    """
    if len(extenstions) > 0:
        return [f for f in os.listdir(dirName) if dirName.splitext(f)[1] in extenstions]
    return os.listdir(dirName)


