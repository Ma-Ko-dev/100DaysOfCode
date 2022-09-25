with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    with open("Input/Letters/starting_letter.txt", mode="r") as file:
        new_text = file.read().replace("[name]", name.strip())

    with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as file:
        file.write(new_text)
