# FIDI, simple multi perpose utility

import sys
import os

# read args from command line
# usage: fidi.py [file or dir] [command] --[option1] [value] --[option2] [value] ...
# example: fidi.py ./images resize --width 100 --height 100 --center --keep-ratio --format png --keep-old

currDir = os.getcwd()

if len(sys.argv) < 2:
    print('usage: fidi.py [file or dir] [command] --[option] [value] ...')
    print('example: fidi.py resize --width 100 --height 100 --center --keep-ratio --format png --keep-old')
    exit()

# get command and args
command = sys.argv[1]

# parse args
args = {}
for i in range(1, len(sys.argv)):
    # check if args[1] is file or dir
    
    if i == 1:
        if os.path.isfile(sys.argv[i]):
            args['file'] = sys.argv[i]
            args['command'] = sys.argv[i+1]
            i += 1
        elif os.path.isdir(sys.argv[i]):
            args['dir'] = sys.argv[i]
            args['command'] = sys.argv[i+1]
            i += 1
        else:
            print('{}를 읽을 수 없습니다.'.format(sys.argv[i]))
            exit()
        continue

    # if no command, exit
    if not 'command' in args:
        print('error: no command specified')
        exit()

    if sys.argv[i].startswith('--'):
        if i + 1 < len(sys.argv) and not sys.argv[i+1].startswith('--'):
            args[sys.argv[i][2:]] = sys.argv[i+1]
            i += 1
        else:
            args[sys.argv[i][2:]] = True    

print(args)

def execProgram():
    if args['command'] == 'imageResize':
        imageResize(args)
    else:
        print('error: no command specified')

def imageResize(args):
    '''
    이미지 크기 변경
    가능한 매개변수
     --size: 실수 또는 [width]x[height] 형식의 문자열
     size > 1.0 이상의 실수이면 확대
     0 < size < 1.0 이면 축소
     w  x y 이면 크기 변경, --crop 옵션이 있을 경우 crop 을 수행
    '''
    import imageResizer as ir
    import fileUtil as fu
    from os import path

    if 'x' in args['size']:
        width = int(args['size'].split('x')[0])
        height = int(args['size'].split('x')[1])
        resize = True
    else:
        ratio = float(args['size'])

    files = []
    if 'file' in args:
        files.append(args['file'])

    if 'dir' in args:
        files += [path.join(args['dir'], f) for f in fu.getImageFilesInDir(args['dir'])]
    
    for f in files:
        print(f)
        ir.resizeImageKeepRatio(f, ratio)

# run exec command
execProgram()