import os

# osモジュールはPythonで非常によく使われる標準ライブラリのひとつで、オペレーティングシステム（Operating System）とのやりとりを可能にするツール
# 名前の通り「OS（オーエス）」に関連する機能を提供します。

# osモジュールとは？
# Pythonのosモジュールは、ファイルやディレクトリの操作、環境変数の取得・設定、プロセス管理などを行うための機能を提供します。
# これにより、Pythonコードから直接OSの機能を使うことができます。

# 1. 📁 ファイル・ディレクトリ操作
# カレントディレクトリの取得
print(os.getcwd())

# ディレクトリの作成
# os.mkdir("new_folder")

# os.path.exists の使い方
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


# 2. 環境変数の操作
os.environ["monty"] = "python"
print(os.environ["monty"])


# 3. コマンドの実行
# OSのコマンドを実行（例：ls）
os.system("ls")