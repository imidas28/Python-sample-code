import os

sample_dir = "C:/tmp/Python-sample-code/sample"
for root, dirs, files in os.walk(sample_dir):
    print("現在のディレクトリ:", root)
    print("サブディレクトリ:", dirs)
    print("ファイル:", files)