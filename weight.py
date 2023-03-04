print("--WELCOME TO MY WEIGHT CONVERTER--")
print("[1] KG to LB")
print("[2] LB to KG")
print("[3] EXIT")


def kilogram_to_pounds(weight):
    return weight / 0.45359237


def pounds_to_kilogram(weight):
    return weight * 0.45359237


user_choice = input("Enter your choice: ")
while user_choice in ['1', '2'] and user_choice != '3':
    try:
        if user_choice == '1':
            weight = float(input("Enter your weight [kg]: "))
            total = kilogram_to_pounds(weight)
            print(f"KG: {weight} | LB: {total}")
        elif user_choice == '2':
            weight = float(input("Enter your weight [lb]: "))
            total = pounds_to_kilogram(weight)
            print(f"LB: {weight} | KG: {total}")
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
        user_choice = input("Enter your choice: ")
    except ValueError:
        print("Please enter a valid input.")
