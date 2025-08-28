# Enumクラスを継承する理由は、そのクラスを「列挙型(Enum)」として機能させるため。

# ✅ 結論：Enum を継承する理由：
# そのクラスのプロパティを「列挙可能な定数」として扱えるようにするため。
# Pythonでは、ただのクラスに定数を並べても、それは「列挙型」としての機能を持たない。
# Eunmを継承することで、以下のような便利な性質が使えるようになる。

from enum import Enum

class Country(Enum):
    CONTRY_1 = "アメリカ"
    CONTRY_2 = "ブラジル"
    CONTRY_3 = "ドイツ"

print(Country.CONTRY_1.name)
print(Country.CONTRY_1.value)


# Enum(列挙型)はあらかじめ決められた選択肢(定数の集合)を定義するための仕組み。
# 上記の例だと:
# Country型を使うと「アメリカ / ブラジル / ドイツ」以外は選べない、という制約になります。

# 曜日の例と同じで、
class Weekday(Enum):
    MON = "月"
    TUE = "火"
    WED = "水"
    THU = "木"
    FRI = "金"
    SAT = "土"
    SUN = "日"

# この場合も「7個のうちのどれか」という選択肢しか取れません。
# つまり、Enum = 限定された選択肢を表す定数の集合という理解でバッチリです。