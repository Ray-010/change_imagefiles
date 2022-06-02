""" 使い方
imagesフォルダ内のpngファイルをjpgファイルに変換します
"""

import os
import glob
from PIL import Image

# png ⇒ jpg変換
path_png = './images/*png'
plist = glob.glob(path_png)
for file in plist:
    img = Image.open(file)
    img = img.convert('RGB')
    save_filepath = file[:-4] + '.jpg'
    img.save(save_filepath, quality = 90)
    os.remove(file)