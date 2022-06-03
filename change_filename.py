""" 使い方
imagesフォルダに名前を変更したいjpg画像を入れてください。
後はこのファイルを実行すれば
pedestrian_light_image + number .jpg

の名前に変更されます
"""

import os
import glob

path_jpg = './images/*.jpg'
flist = glob.glob(path_jpg)

# 画像名前の変更
file_name = 'a_pedestrian_light_image'
for i, file in enumerate(flist):
    print(file)
    os.rename(file, './images/' + file_name + str(i) + '.jpg')
