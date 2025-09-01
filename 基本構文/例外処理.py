# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(f"エラーが発生しました: {e}")

try:
    membership_no = input("会員番号を入力してください。\n")
    print(f"1: 入場規制について, 2: 料金について, 3: その他")
    inquiry_num_str = input("1～3のうちいずれかの値を入力してください:\n")
    inquiry_num = int(inquiry_num_str)

    members = {
        "391028": "山田太郎",
        "920928": "斎藤花子",
        "459033": "小池優斗"
    }
    
    member_name = members[membership_no]

    if inquiry_num == 1:
        answer = f"混雑規制のため、{int(inquiry_num) * 10}のゲートから入場してください"
    elif inquiry_num == 2:
        answer = "料金は当日お伝えします"
    elif inquiry_num == 3:
        answer = "用件をお伝えください"
    print("=" * 10)
    print()

except IndexError as e:
    print(e)
