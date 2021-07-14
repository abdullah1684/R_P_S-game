def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def divide(x, y):
    return x / y


print("""Choose:
1 --> For add
2 --> for Subtract
3 --> For multiply
4 --> For Divide

""")

choose = input("Your Choice: ")

num1 = int(input("Number1: "))
num2 = int(input("Number2: "))


if choose == "1":
    result = add(num1, num2)
    print(result)

elif choose == "2":
    result = sub(num1, num2)
    print(result)

elif choose == "3":
    result = multi(num1, num2)
    print(result)

elif choose == "4":
    result = divide(num1, num2)
    print(result)

else:
    print("Invalid Input")