list = [
    {"name": "田中太郎", "age": 41},
    {"name": "佐藤花子", "age": 20},
    {"name": "鈴木一郎", "age": 51},
    {"name": "高橋美咲", "age": 19},
    {"name": "伊藤健一", "age": 39},
    {"name": "山本紗英", "age": 24},
    {"name": "中村翔太", "age": 26},
    {"name": "小林恵", "age": 42},
    {"name": "渡辺直樹", "age": 58},
    {"name": "松本陽子", "age": 33}
]

new_list = [ele for ele in list if ele["age"] <= 20]
print(new_list)
print(new_list[0]["name"]) #個別の要素の"name"キーの値を抽出

# リスト内包表記
# 1.for ele in listで、元のリストの各要素（辞書型）を順に取り出す。
# 2.if ele["age"] <= 20で、条件を満たす要素のみをフィルタリングする。
# 3.ele["name"]はforの直前で指定された値です。この値が条件を満たした場合、新しいリストにそのまま格納される。


# new_listには条件式に一致する要素だけが格納される。