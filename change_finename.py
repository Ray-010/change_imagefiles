""" 使い方
imagesフォルダに名前を変更したいjpg画像を入れてください。
後はこのファイルを実行すれば
pedestrian_light_image + number .jpg

の名前に変更されます
"""

import os
import glob

# 画像名前の変更
path_jpg = './images/*.jpg'
flist = glob.glob(path_jpg)
print(flist)
for i, file in enumerate(flist):
    print(file)
    os.rename(file, './images/a_pedestrian_light_image' + str(i) + '.jpg')
