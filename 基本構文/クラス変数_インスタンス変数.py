# クラス変数（class variable）
# ・クラス直下に定義された変数
# ・インスタンス化しなくても、クラス名.クラス変数名でアクセス出来る。
# ・全インスタンスで共有される
# ・Pythonではインスタンスからでもクラス変数にアクセス出来る。

class MyClass:
    class_var = "共通の値"

print(MyClass.class_var)

a = MyClass()
b = MyClass()
print(f"a: {a.class_var}") # "共通の値"
print(f"b: {a.class_var}") # "共通の値"

# 変更すると全インスタンスに影響
MyClass.class_var = "変更されました"
print(f"a: {a.class_var}")
print(f"b: {a.class_var}")



# インスタンス変数
# ・インスタンスごとに持つ変数
# ・通常は、__init__内で、self.変数名 = 値 として作られる。
# ・インスタンス化しないと使えない。
# ・各インスタンスで独立した値を持っている。

class MyClass2(MyClass):
    def __init__(self, name): # 初期化メソッド(コンストラクタ)
        self.name = name # インスタンス変数


c = MyClass2("Alice")
d = MyClass2("Bob") 

print(c.name)
print(d.name)
print(f"c: {c.class_var}")
print(f"d: {d.class_var}")

# クラスをインスタンス化しないと使えないクラスで、主にメソッド内にある変数
# 正確にはself.〇〇と書かれたものがインスタンス変数