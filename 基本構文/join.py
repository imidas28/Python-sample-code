# joinメソッド
# Pythonの文字列メソッドで、イテラブル（リストやタプルなど）に含まれる要素を、
# 指定した文字列で連結して1つの文字列にする処理。

# 基本形
# "区切り文字".join(イテラブル)

items = ["A", "B", "C"]
result = "-".join(items)
print(result)

# "区切り文字"の部分が"A" と "B" と "C" の間に入るイメージです。
# 注意点: join対象は 文字列のリスト（またはイテラブル） でなければなりません。（数値や辞書などを含むとエラーになります）


destination = ["東京", "大阪", "名古屋"]
destination_str = "\n".join(destination)
print(destination_str)
print(type(destination_str))