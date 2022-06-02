""" 使い方
imagesフォルダ内のjpgファイルをアスペクト比固定で
max_height = 720
max_width = 1280
で縮小します
"""

import glob
from PIL import Image

# アスペクト比固定で画像リサイズ
path_jpg = './images/*.jpg'
flist = glob.glob(path_jpg)
max_height = 720
max_width = 1280
for file in flist:
    img = Image.open(file)
    ok = False
    
    if img.width > img.height:
        if img.width >= max_width:
            width = max_width
            height = int(img.height / (img.width/max_width))
            ok = True
    else:
        if img.height >= max_height:
            height = max_height
            width = int(img.width / (img.height/max_height))
            ok = True

    if ok:
        print("resized", file, "height: ", height, "width: ", width)
        img_resized = img.resize((width, height))
        img_resized.save(file, quality = 90)
