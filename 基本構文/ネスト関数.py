# ネスト関数の例

def outside():
    def inside():
        print("内側の関数です")
    print("外側の関数です")
    inside()

outside()


# ネスト関数のクロージャ(closure)は、外側の関数の変数を「内側の関数が覚えて使える」機能。
def outer(x):
    def inner(y):
        return x + y # outerの変数 x を inner関数が覚えている。
    return inner # inner関数を返す


f = outer(10)
print(f(5))

# ・ここでouter(10)を実行すると、x = 10がセットされる。
# ・outer関数は戻り値がinner関数そのものを返す。
# (このときx = 10という値を覚えた状態で返す → これがクロージャ)
# 変数fにはinner関数が格納されている。