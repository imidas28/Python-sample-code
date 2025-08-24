# Pythonでは「繰り返し可能なオブジェクト」のことをイテラブル(iterable)と呼ぶ。

# 1.イテラブルとは
# forループで順番に取り出せるオブジェクトのこと。
# 内部に__iter__()メソッドが定義されているオブジェクト

# リストはイテラブル
data = [1, 2, 3]
for i in data:
    print(i)

# タプルもイテラブル
t = (4, 5, 6)
for i in t:
    print(i)

# 文字列もイテラブル
str = "Python"
for i in str:
    print(i)


# 2.イテラブルかどうかを確認する
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))
print(isinstance("Python", Iterable))
print(isinstance(100, Iterable))