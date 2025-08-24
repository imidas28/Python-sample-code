template = """
以下の食材と料理ジャンルにおける、その食材を使ったユニークな料理アイデアを3つ教えてください。

食材: {ingredients}
料理ジャンル: {cooking_genre}
"""

# {ingredients}, {cooking_genre}, {format_instruction} はプレースホルダー(後から値を埋め込む部分)

message = template.format(ingredients="トマト", cooking_genre="イタリア料理")
print(message)


# ポイント:
# プレースホルダーに値を入れる操作を 「フォーマット」 と呼ぶ
