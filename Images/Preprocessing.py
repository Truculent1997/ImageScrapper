import os
from glob import glob
from PIL import Image
import cv2
def resizeandrotate():
    path = "WithoutNotes/"
    os.chdir(path)
    #Image Rotation
    pngs = []
    type = ('*.jpg')
    pngs.extend(glob(type))
    for img in pngs:
        image = Image.open(img)
        imageresize = image.resize((250, 250), Image.ANTIALIAS)
        file, extension = os.path.splitext(img)
        imageresize = imageresize.convert('RGB')
        imageresize.save(file + 'a' + extension, 'JPEG', quality=90)
        imageresize.rotate(90).save(file + 'b'+extension, 'JPEG', quality=90)
        imageresize.rotate(180).save(file + 'c'+extension, 'JPEG', quality=90)
        imageresize.rotate(270).save(file + 'd'+extension, 'JPEG', quality=90)
        if os.path.exists(file + 'a'):
            os.remove(file + 'a')
        if os.path.exists(file + 'b'):
            os.remove(file + 'b')
        if os.path.exists(file + 'c'):
            os.remove(file + 'c')
        if os.path.exists(file + 'd'):
            os.remove(file + 'd')
        if os.path.exists(img):
            os.remove(img)

def removenoisewithgaussian():
    path = "WithoutNotes/"
    os.chdir(path)
    pngs = []
    type = ('*.jpg')
    pngs.extend(glob(type))
    for img in pngs:
        image=cv2.imread(img)
        file, extension = os.path.splitext(img)
        gausBlur=cv2.GaussianBlur(image,(9,9),0)
        filename=(file+extension)
        print(filename)
        if os.path.exists(img):
            os.remove(img)
        status=cv2.imwrite(filename, gausBlur)


if __name__=='__main__':
    #resizeandrotate()
    #removenoisewithgaussian()
