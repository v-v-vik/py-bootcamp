import pandas

nato_alph_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alph_dict = {row.letter:row.code for (index, row) in nato_alph_df.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [nato_alph_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
