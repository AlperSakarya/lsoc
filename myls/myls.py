import os
import sys

def myls():
    if not len(sys.argv) >1:
        myls = 'stat -c "%a %n" *'
        os.system(myls)
    else:
        myFile = str(sys.argv[1])
        myls = 'stat -c "%a %n" {0}'.format(myFile)
        os.system(myls)

myls()

__author__ = 'Alper Sakarya'
