# 出力が
# Document(metadata={...}, page_content="...")
# のように Documentというクラス名で始まっているので、Documentオブジェクトだと判断出来る。

# Document(
#     page_content="ここに本文テキスト",
#     metadata={
#         "title": "記事タイトル",
#         "post": "投稿情報",
#         "source": "https://example.com"
#     }
# )

# LangChainのDocumentオブジェクトは
# 第1階層 → Document オブジェクト
# page_content （本文テキスト、文字列型）
# metadata （メタデータ、辞書型 dict）
# という 2つの属性（プロパティ） を持っています。

# さらに分解すると
# metadataの値は{...}(辞書オブジェクト)
# つまり、metadataはネストされたオブジェクトであり、その中にさらにキーと値が入っている構造になる。