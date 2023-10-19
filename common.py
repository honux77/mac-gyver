# CLI에 사용되는 공통 기본 모뮬

import os
import sys

def readArgs(numArgs, errorMsg):
    """
    Reads the arguments from the command line
    """
    if len(sys.argv) != numArgs + 1:
        print(errorMsg)
        sys.exit(1)
    return sys.argv[1:]
