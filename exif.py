import os
import PIL
import glob
import sys
from core.help  import helpsnippet
from core.scrambler import scrambler


def motor():
    print("motor")
    scrambler.helo()

def help():
    #banner
    helpsnippet.show()


    
def init():
    if(len(sys.argv) < 2):
        help()
    else:
        motor()




if __name__ == '__main__':
    init()