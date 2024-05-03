# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_words = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_words)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def create_phonatic():
    user_word = [letter.upper() for letter in input("Enter any word : ")]
    try:
        phonetic_word = [nato_words[letter] for letter in user_word]
    except KeyError:
        print("Please provide alphabetical input.")
        create_phonatic()
    else:
        print(phonetic_word)

create_phonatic()
