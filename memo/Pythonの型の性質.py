# Pythonの型の性質
# Pythonは動的型付け言語
# 実際に代入される値によって型が決まる。
# 例えば、x = 10のあとに、x = "おはよう"と書いてもエラーにならない。

# prompt: PromptTemplate = prompt について
# : PromptTemplate ⇒ 型ヒント
# = prompt ⇒ 実際の代入

# 重要ポイント
# : PromptTemplate は 型を強制しているわけではない
# 実行時には 無視される（型チェックは行われない）
# # ただし mypy や Pyright のような静的型チェッカーや、IDE（VSCode など）の補完で使われる

from typing import List

nums: List[int] = [1, 2, 3]
nums = "文字列" # 実行時にはエラーにならない(型は無視される)
