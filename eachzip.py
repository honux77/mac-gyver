'''
eachzip.py
Compresses each file in a directory into a zip file
'''
import os
from os import path

from fileUtil import getfilesInDirectory

def generateZipfile(zipFileName, files):
    '''
    Generates a zip file from files
    '''
    import zipfile
    for f in files:
        if not os.path.isfile(f):
            raise Exception('File ' + f + ' does not exist')
    z = zipfile.ZipFile(zipFileName, 'w')
    for f in files:
        z.write(f)
    z.close()    
    
def archiveEachFilesInDir(dirName, deleteOriginal = False):
    """Compresses all files in a directory"""
    print('Compressing files in directory: ' + dirName)
    if not path.isdir(dirName):
        raise Exception(f'Directory {dirName} does not exist')
    
    for f in getfilesInDirectory(dirName):
        fullPath = path.join(dirName, f)
        if path.isfile(fullPath) or path.splitext(f)[1] == '.zip':
            print('Compressing file: ' + fullPath)
            # get the file name without the extension
            zipFileName = path.splitext(f)[0] + '.zip'
            generateZipfile(path.join(dirName, zipFileName), [fullPath])
            if deleteOriginal:
                print('Deleting: ' + fullPath)
                os.remove(fullPath)
        else:
            print('Skipping: ' + fullPath)

if __name__ == '__main__':
    import common     
    args = common.readArgs(1, 'Usage: eachzip.py <directory>')
    try: 
        archiveEachFilesInDir(args[0], True)    
    except Exception as e:
        print(e)
        exit(1)
    print('Done')