# FIDI, simple multi perpose utility

import sys
import os

currDir = os.getcwd()

import imageResizer

# get command and args
yes = len(sys.argv) > 1 and sys.argv[1] == '-y'

# read other args from env
import envi
envi.readEnv()

# check file or dir exists
if not os.path.exists(envi.env['dir']):
    print('error: file or dir not exists')
    exit()

# if not yes, ask for confirmation
if not yes:
    print("환경변수: ", envi.env)
    # print full path of env.json
    print("환경변수를 고치고 싶으면 {} 파일을 수정하세요.   ".format(os.path.join(currDir, 'env.json')))
    print('실행하시겠습니까? (y/N)')
    if input() != 'y':
        exit()

def imageResize(envs):
    '''
    이미지 크기 변경
    가능한 매개변수
    ratio: 0.0 < ratio < 1.0 이면 축소, ratio > 1.0 이면 확대
    size: w x h 이면 크기 변경, --crop 옵션이 있을 경우 crop 을 수행     
    '''
    import imageResizer as ir
    import fileUtil as fu
    from os import path

    resize = 'resize' in envs
    crop = 'crop' in envs  
    cropCenter = 'cropCenter' in envs           

    if 'size' in envs:
        width = int(envs['size'].split('x')[0])
        height = int(envs['size'].split('x')[1])    
                    
    elif 'ratio' in envs:
        ratio = envs['ratio']
    else:
        print('error: size 나 ratio 를 지정하세요.')
        exit()
    
    files = []

    if 'file' in envs:
        files.append(envs['file'])

    if 'dir' in envs:
        files += [path.join(envs['dir'], f) for f in fu.getImageFilesInDir(envs['dir'])]
    
    for f in files:
        print("Start Resizing: ", f)

        if not resize:
            ir.resizeImageKeepRatio(f, ratio)
        elif resize and not crop:
            ir.resizeImage(f, width, height)
        else:
            ir.cropImage(f, width, height, 'center' in envs)


# run commands
commands = {
    'resize': imageResize,
}


# if command is not in commands
command = envi.env["command"]
if not command in commands:
    print('error: command not exists')
    exit()

commands[command](envi.env)