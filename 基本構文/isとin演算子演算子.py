# is演算子は「オブジェクトが同一化どうか」を比較する演算子。

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True ⇒ 同じオブジェクト
print(a is c) # False ⇒ 中身は同じでも別オブジェクト

# a is bはaとbがメモリ上で同じオブジェクトかをチェック
# a == cなら中身が同じかどうかをチェックする比較する演算子



# inは「文字列の中に特定の文字列があるか判定する場合」
# 以下の場合はinを使う。

# 1. 文字列に含まれるかどうか
s = "hello world"

print("hello" in s) # True
print("bye" in s) # False


# 2.リストやタプルに要素が含まれているかどうか
nums = [1, 2, 3, 4, 5]
print(3 in nums) # True
print(10 in nums) # False


# 3.辞書にキーが含まれているどうか
person = {"name": "Alice", "age": 30}
print(f"name: {'name' in person}")
print(f"job: {'job' in person}")