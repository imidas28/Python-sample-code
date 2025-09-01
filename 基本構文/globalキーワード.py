x = 10

def foo():
    global x
    x = 20 # これでグローバル変数 x を更新出来る

foo()
print(x) # 20


# 1.globalキーワードの意味
# Pythonでglobalを使うのは関数の中からモジュールスコープ(トップレベルスコープ)の変数を参照・更新したいとき。
# もしglobalを書かないで関数の中で、x = 20とすると、Pythonは「新しいローカル変数 x が作られた」と解釈するので、
# グローバルのxは書き換わない。

# 2.「なぜ global service_doc_chain_chat_history = [] としないのか？」
# 理由は単純で、Pythonの構文として許されないからです。

# global 文の構文は：
# global var1, var2, ...
# のみであり、代入を伴うことは出来ない。

# つまり
# global service_doc_chain_chat_history = []
# は文法エラーになる。