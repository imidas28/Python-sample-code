# 1.Noneの意味
# ・「値が存在しないこと」を表す特別なオブジェクト
# ・型はNoneType
# ・つまり、変数がまだ値を持っていない、あるいは「空」という状態を明示するために使う。

# x = None
# print(x)
# print(type(x))


# 2.具体的な使い方
# ・初期化に使う:
# 変数に後で値を代入する前に「まだ何も入っていない」と明示したい場合

db = None # データベースオブジェクトはまだ作られていない。

# 後で必要になったときに作成
if db is None:
    db = "DBを作成しました"

print(db)

# 関数の戻り値で使う
# 何も返す必要がない場合や、条件によって値がないことを示すとき。

def find_item(lst, target):
    for item in lst:
        if item == target:
            return item
    return None # 見つからなかった場合

result = find_item([1, 2, 3], 3)
print(result)

result = find_item([1, 2, 3], 4)
print(result)


# デフォルト引数として使う
def greet(name=None):
    if name is None:
        print("こんにちは、ゲストさん")
    else:
        print(f"{name}さん、こんにちは")

greet()
greet("金井")
