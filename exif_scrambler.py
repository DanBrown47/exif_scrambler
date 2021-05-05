from __future__ import print_function

import os
import PIL
import glob
import sys
import argparse
from core.help  import helpsnippet
from core.scrambler import scrambler



def help():
    helpsnippet.show()

def arg_proc_engine():
    flag = sys.argv[1]
    parser = argparse.ArgumentParser(description='Parse flags of the scrambler')
    parser.add_argument('-s','--scramble',type=str,help='Image name',dest='img_ogi')
    
    args = parser.parse_args()
    filename = args.img_ogi
    scrambler.helo(filename)

    
       
def init():
    if(len(sys.argv) < 2):
        help()
    else:
        arg_proc_engine()

if __name__ == '__main__':
    init()