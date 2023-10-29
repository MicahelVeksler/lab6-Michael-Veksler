
def encode_password(password):
    encoded = ""

    if len(password) < 8:
        password = "0" * (8 - len(password)) + password

    for i in password:
        encoded_dig = str((int(i) + 3) % 10)
        encoded += encoded_dig
    return encoded
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

while True:
    menu()
    choice = int(input("Please enter an option:"))

    if choice == 1:
        password = input("Please enter your password to encode:")
        print("Your password has been encoded and stored!")

