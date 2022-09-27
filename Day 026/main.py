import pandas

DATA = "data/nato_phonetic_alphabet.csv"

nato_data = pandas.read_csv(DATA)
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

word = input("Please enter a Word: ").upper().strip()
word_to_nato = [nato_dict[letter] for letter in word]

print(word_to_nato)
