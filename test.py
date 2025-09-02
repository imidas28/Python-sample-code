import os

docments = []
for filename in os.listdir("sample"):
    # print(filename)
    filepath = os.path.join("sample", filename)
    print(filepath)
    root, ext = os.path.splitext(filename)
    print(root)
    print(ext)

# splitextメソッドの戻り値はタプル(root, ext)
# root: 拡張子を除いたファイル名
# ext: 拡張子(ドット.付き)