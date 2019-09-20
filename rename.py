# rename.py

import glob
import os
import sys

indir = sys.argv[1]
prefix = sys.argv[2]

# ディレクトリ下のファイル名を再帰的に取得する
path = os.path.join(indir, "**/*.*")
all_imgs = glob.glob(path, recursive=True)
all_imgs.sort()
# ファイル数が何桁か調べる
digit = len(str(len(all_imgs)))

for index, img in enumerate(all_imgs, 1):
    # 元のディレクトリ構造とファイル名、拡張子を取得する
    ori_dir, ori_name = os.path.split(img)
    filename, suffix = os.path.splitext(ori_name)
    # 自分自身はリネームしない
    if ori_name == "rename.py":
        continue
    # 通し番号の桁を揃える
    num = str(index-1)
    # 新しいファイル名の生成、ディレクトリと拡張子は元のまま
    new_name = "{0}{1}".format(num, suffix)
    new_path = os.path.join(ori_dir, new_name)
    # 変更後と同じ名前のファイルが存在する場合はスキップ
    if os.path.exists(new_path):
        sys.stderr.write(
            "{0} already exists\n".format(new_path))
        continue
    # リネーム
    os.rename(img, new_path)
    print("{0} -> {1}".format(ori_name, new_name))
