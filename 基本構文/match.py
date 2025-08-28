user_input = input("a, b, cいずれかの値を入力してください\n")

try:
    match user_input:
        case "a":
            print("Aです")
        case "b":
            print("Bです")
        case "c":
            print("Cです")
except ValueError as e:
    print("不正な値です")