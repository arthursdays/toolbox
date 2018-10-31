import os
from shutil import copyfile
import random

typename="Tinea_Corporis"

filedir = os.path.join('/home/arthur/Documents/derm101', typename)
outputdir = os.path.join(filedir, 'selected')



filelist = []
settocopy = set()

for file in os.listdir(filedir):
    if not os.path.isdir(os.path.join(filedir, file)):
        print(file)
        filelist.append(file)

while len(settocopy) < min(400, len(filelist)):
    settocopy.add(filelist[random.randint(0, len(filelist)-1)])

if not os.path.exists(outputdir):
    os.makedirs(outputdir)

for file in settocopy:
    copyfile(os.path.join(filedir, file), os.path.join(outputdir, file))

