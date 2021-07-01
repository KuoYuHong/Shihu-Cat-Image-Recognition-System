# 抓取臉部特徵

from PIL import Image
import os
import cv2 as cv

def extractFace(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
        
    for f in os.listdir(src_dir):
        filename = src_dir + f
        img = Image.open(filename)
        imgary = cv.imread(filename)
        face_cascade = cv.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
        faces = face_cascade.detectMultiScale(imgary, scaleFactor=1.3, minNeighbors=1)
        if len(faces) == 1:
            x,y,w,h = faces[0]
            crpim = img.crop((x,y, x + w, y + h)).resize((64,64))
            crpim.save(dest_dir + f)

if __name__ == '__main__':
    ###extractFace參數中如有任何中文路徑則無法使用

    extractFace('catbody/', 'catface1.3-1/') #虎斑貓
    # extractFace('shihubody/', 'shihuface1.3-1/') #石虎
