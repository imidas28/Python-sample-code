import os

# 1. os.path.exists の使い方
# Python の標準ライブラリ os に含まれる関数で、指定したパスが「存在するかどうか」を判定するものです。

path = "../test.txt"

if os.path.exists(path):
    print("このパスは存在します")
else:
    print("このパスは存在しません")


# ・戻り値: True または False
# ・ファイルでもフォルダでも存在すれば True になります。
# ・os.path.isdir(path) → 「存在して、かつディレクトリなら True」
# ・os.path.isfile(path) → 「存在して、かつファイルなら True」