#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt", "r") as mail_format:
    mail_formats = mail_format.read()
    print(mail_formats)

with open("./Input/Names/invited_names.txt", "r") as names:
    mail_names = names.readlines()
    print(mail_names)
    for name in mail_names:
        stripped_name = name.strip()
        new_letter = mail_formats.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}_mails.txt", "w") as mail_examples:
            mail_examples.write(new_letter)
