# Pythonでいうパース(parse)は、
# 「ある形式で書かれたデータや文字列を、プログラムが扱いやすい構造に変換すること」

# 1.パースのイメージ:
# 人間にとって
# りんご 3個
# というメモはすぐ分かりますが、コンピュータにとってはただの文字列"りんご 3個"です。
# これをプログラムで扱いやすい形に変換すると、
# {"fruit": "りんご", quantity: 3}

# 2.よくあるパースの例:
# 例1: JSONのパース
# Web APIのレスポンスはJSON文字列のことが多い。

import json

# 文字列としてのJSON
json_str = '{"name": "Alice", "age": 25}'

# パースして辞書型に変換
data = json.loads(json_str) # json.loadsは文字列をパースして辞書型に変換

print(data["name"])
print(data["age"])


# 例3: 独自フォーマットのパース
text = "fruit=apple;quantity=5"

# パースして辞書型に変換
pairs = text.split(";")
result = {}

for pair in pairs:
    key, value = pair.split("=")
    result[key] = value

print(result["fruit"])
print(result["quantity"])

# key, value = pair.split("=")
# 上記の書き方は、分割代入(アンパック代入)という。
# pair.split("=")は"fruit=apple" のような文字列を["fruit", "apple"]というリストに変換する。
# その結果をkey, value = ["fruit", "apple"]
# のようにリスト(タプル)の各要素を左辺の変数に順番に代入していく。


# パース(parse): 「解析する」という動作・行為
# パーサー(parser): 「解析するもの」という役割を持つ仕組みやプログラム
# 身近な例え
# パース → 料理を作るという行為
# パーサー → 料理を作る人や調理器具