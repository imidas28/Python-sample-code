# イテレーター(iterator)
# ・次の要素を1つずつ取り出せるオブジェクト
# ・__iter__()と__next__()を持つ。
# ・iter(イテラブル)を呼ぶと、イテラブル⇒イテレーターに変換できる。
# ・next(イテレーター)で要素を順番に取り出す。


data = [10, 20, 30]
it = iter(data)

print(next(it))
print(next(it))
print(next(it))