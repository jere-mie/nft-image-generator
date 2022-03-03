from os import listdir
from os.path import isfile, join
import os
mypath = './out/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

curr = 1
for file in onlyfiles:
    if file != 'README.md':
        os.rename(mypath+file, f'{mypath}{curr}.png')
        curr+=1

print(f'{curr-1} images renamed')
