# プログラミングにおける「イディオム」とは、
# その言語でよく使われる「お決まりの書き方」や「慣用的な表現」のこと

# 例題：
def get_data():
    return {"user": "太郎", "history": "これは会話履歴です"}


# イディオムを使わない(分かりやすい書き方)
result = get_data() # 関数の戻り値を変数に格納
print(result["user"]) # キーで値を取り出す

# イディオムを使う(まとめて書く)
result = get_data()["history"] # これは会話履歴です
print(result)