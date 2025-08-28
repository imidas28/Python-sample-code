# from openai import OpenAI
# openaiという名前のライブラリ(パッケージ)からOpenAIという名前の「クラス」や「関数」などの
# オブジェクトをインポート(エクスポートしたデータを読み込む)しているという意味
# ・openai: インストールされたライブライ(パッケージ)
# ・OpenAI: その中に定義されているクラス、関数、定数などの名前


# 例で理解しよう
# もし openai ライブラリの中に次のような構造があると仮定すると：
# そして api.py の中に OpenAI クラスが定義されていれば、
# from openai import OpenAI はそれをインポートしていることになります。

# openai/
# ├── __init__.py
# ├── api.py
# └── models.py

# 🎯 Pythonで最も基本的なライブラリのインポートと使用方法は、次のような構文になります：
# import ライブラリ名
# ライブラリ名.関数名(引数)
# このスタイルは、ライブラリ全体をインポートして、その中の関数やクラスを使うという方法です。

#🧪 例：mathライブラリ
import math

result = math.sqrt(16)
print(result)  # 出力: 4.0

# math：Python標準ライブラリ
# sqrt：平方根を計算する関数
# math.sqrt(16)：mathライブラリの中のsqrt関数を使っている

# キーワード引数とは、引数を渡す際に値だけでなく、「引数名=値」の形式で引数名を指定して渡す機能です。

# Pythonのimport文における「ドット(.)」は、モジュールの階層構造(パッケージの中のサブパッケージやモジュール)を表している。
# langchain.schema の意味
# ・langchain はライブラリ全体のトップレベルパッケージ
# ・schema はその中にある サブパッケージまたはモジュール
# ・SystemMessage, HumanMessage: これらはlangchain.schemaモジュール内のクラスまたはオブジェクトです。