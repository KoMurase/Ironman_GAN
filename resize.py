# -*- coding: utf-8 -*-
import os
import glob
from PIL import Image

# Setting(ここを変更して希望のサイズに変換)
dir_location =r'C:\Users\mkou0\Desktop\Ironman\mycrawler\images\full' #変換したい画像ファイルがあるフォルダを指定 ['']内を変更
save_location =r'C:\Users\mkou0\Desktop\Ironman\mycrawler\images\output' #変換した画像ファイルを保存するフォルダを指定　['']内を変更
ratio_fixed = 1 #縦横比を固定する場合は、1 しない場合は 0
width = 100  #画像の横サイズ
height = 100  #画像の縦サイズ

# 取得ファイル形式一覧
ext_list =('/*.jpg','/*.jpeg','/*.gif','/*.png')   #

for n in range(len(ext_list)):
    file_path = dir_location + ext_list[n]
    file_list = glob.glob(file_path)
    for f in file_list:
        img = Image.open(f)
        if ratio_fixed == 1:
            img.thumbnail((width, height))
        else:
            img = img.resize((width, height))
        full_file, ext = os.path.splitext(f)
        name = os.path.basename(full_file)
        img.save(save_location +'/'+ name + ext)
        print(name+'変換完了!')
print('画像の変換完了')
