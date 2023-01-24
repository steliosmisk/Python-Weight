print("--WELCOME TO MY WEIGHT CONVERTER--")
print("[1] KG to LB")
print("[2] LB to KG")
print("[3] EXIT")


def kilogram(weight):
    return weight // 0.45359237


def pounds(weight):
    return weight * 0.45359237


user_choice = input("Enter your choice: ")
while user_choice in ['1', '2'] and user_choice != '3':
    if user_choice == '1':
        weight = float(input("Enter your weight [kg]: "))
        total = kilogram(weight)
    else:
        weight = float(input("Enter your weight [lb]: "))
        total = pounds(weight)
    print(f"KG: {weight} | LB: {total}")
    break

