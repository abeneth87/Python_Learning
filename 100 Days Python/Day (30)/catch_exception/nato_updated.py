# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

# Read the NATO phonetic alphabet CSV into a DataFrame
nato_df = pd.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary from the DataFrame where keys are letters and values are NATO codes
nato_dict = {row['letter']: row['code'] for _, row in nato_df.iterrows()}
print(nato_dict)

def generate_phonetic():
    name = input("Enter your name: ").upper()
    try:
        phonetic_code = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet are supported.")
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()
