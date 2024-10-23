def encode(password):
    res = ""
    for dig in password:
        dig = int(dig)
        new_dig = dig + 3
        if new_dig == 10:
            new_dig = 0
        elif new_dig == 11:
            new_dig = 1
        elif new_dig == 12:
            new_dig = 2
        res += str(new_dig)
    return res


def decode(enc_password):
    res = ""
    for dig in enc_password:
        dig = int(dig)
        if dig == 2:
            dig = 9
        elif dig == 1:
            dig = 8
        elif dig == 0:
            dig = 7
        else:
            dig -= 3
        res += str(dig)
    return res


if __name__ == '__main__':
    repeat = True
    while repeat is True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            enc_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            print(f"The encoded password is {enc_password}, and the original password is {password}.")
            print()
        elif option == 3:
            repeat = False