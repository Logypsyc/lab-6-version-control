# Created by Kenneth Lin
# Function to encode a password by shifting each digit up by 3
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # Shift each digit up by 3 numbers
        encoded_password += encoded_digit

    return encoded_password


def decode(password):
    return ''.join(str(int(c)-3 % 10) for c in password)


# Main function to interact with the user
def main():
    while True:  # Infinite loop for the menu
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("\nPlease enter an option: "))  # Get user's choice
        match choice:
            case 1:
                password = input("Please enter your password to encode: ")
                encoded_password = encode(password)  # Encode the password
                print("Your password has been encoded and stored!")
            case 2:
                pass
                # TODO: implement decoding of the password
            case 3:
                exit()  # Exit the program


if __name__ == '__main__':
    main()
