from glob import  glob
import cv2
import os
from PIL import Image
types = ('*.png', '*.jpeg','*.gif')
pngs=[]
for files in types:
    pngs.extend(glob(files))
for j in pngs:
    file_name=j.lstrip('.\\')
    print(j)
    image=Image.open(file_name)
    image=image.convert('RGB')
    file_ext = os.path.splitext(file_name)[1]
    if file_ext=='.jpeg':
        image.save(file_name[:-4]+'jpg')#Saving in the file with .jpg extension

    elif file_ext == '.gif':
        image.save(file_name[:-3] + 'jpg')  # Saving in the file with .jpg extension

    else:
        image.save(file_name[:-3] + 'jpg')  # Saving in the file with .jpg extension
    os.remove(file_name)#Deleting all types files