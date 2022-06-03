""" 使い方
imagesフォルダ内のjpgファイルをアスペクト比固定で
max_height = 720
max_width = 1280
で縮小します

画像サイズが640を下回る場合は削除します
"""

import os
import glob
from PIL import Image


# アスペクト比固定で画像リサイズ
path_jpg = './images/*.jpg'
flist = glob.glob(path_jpg)
max_height = 720
max_width = 1280
min_height = 640
min_width = 640

for file in flist:
    img = Image.open(file)
    img_width = img.width
    img_height = img.height
    ok = False

    # サイズが小さいときは削除
    if img_width < min_width and img_height < min_height:
        img.save(file)
        os.remove(file)
        print('Deleted', file, ": this image size is too small")
        continue
    
    # 画像のリサイズ
    if img_width > img_height:
        if img_width > max_width:
            width = max_width
            height = int(img_height / (img_width/max_width))
            ok = True
    else:
        if img_height > max_height:
            height = max_height
            width = int(img_width / (img_height/max_height))
            ok = True

    if ok:
        img_resized = img.resize((width, height))
        img_resized.save(file, quality = 90)

        print("Resized", file, "height: ", height, "width: ", width)
