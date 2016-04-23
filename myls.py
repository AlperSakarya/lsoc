import os
import sys

myFile = str(sys.argv[1])


if not myFile:
    myls = 'stat -c "%a %n" *'
    os.system(myls)
else:
    myls = 'stat -c "%a %n" {0}'.format(myFile)
    os.system(myls)

__author__ = 'Alper Sakarya'
