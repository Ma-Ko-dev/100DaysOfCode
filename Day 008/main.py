import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
run = True


def caesar(user_text, user_shift, operation):
    cipher_text = ""
    direction_text = ""
    user_shift = user_shift % 26
    for letter in user_text:
        if operation == "encode":
            if letter not in alphabet:
                cipher_text += letter
            else:
                cipher_text += alphabet[alphabet.index(letter) + user_shift]
                direction_text = "encoded"
        else:
            if letter not in alphabet:
                cipher_text += letter
            else:
                cipher_text += alphabet[alphabet.index(letter) - user_shift]
                direction_text = "decoded"
    print(f"Your {direction_text} Text is: {cipher_text}")


while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(user_text=text, user_shift=shift, operation=direction)

    keep_running = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if keep_running == "no":
        run = False
        print("Goodbye")
