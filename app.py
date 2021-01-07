row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]


player = ["X", "Y"]


def display(row1, row2, row3):
    print(row1)
    print(row3)
    print(row3)


def get_user_input(text):
    print(player)
    valid_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    user_input = input(text)
    if user_input in valid_inputs:
        return int(user_input)
    else:
        return get_user_input("Please enter a number (1 - 9): ")


user_input = get_user_input("Enter number: ")
print(user_input)


display(row1, row2, row3)
