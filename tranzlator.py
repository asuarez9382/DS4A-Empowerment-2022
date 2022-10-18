"""
This is a template script. Please work off of this.
To test the functionality of the script as you build
it, you can run this by opening a terminal, using 
"cd encryption_project_fellow" and then running 
"python tranzlator.py".

Do NOT change the name of any of the files in the
zipped folder. If you do, the autograder will error out
and your project will receive a failing grade.

Your name:Adrian Suarez
Your e-mail:asuarez9382@gmail.com
Date finished: 9/23/2022
"""

# Step 1
# Import the english.txt file
def opens_file(text_file):
    file = open(text_file, "r")
    text = file.readlines()
    return text

text = opens_file("english.txt")

# Step 2
# Import the glossary (the tranzlashun.json file)
# This dataset originally comes from the GitHub repository
# at https://github.com/irdumbs/Dumb-Cogs and is covered by an MIT license

import json 
json_file = open('tranzlashun.json')
  
cat_speak_dictionary = json.load(json_file)

# Step 3
# Translate the English text into Lolspeak

#Puts everything in lowercase

lower_text = [x.lower() for x in text]

#gets rid of \n


clean_text = []
for line in lower_text:
    line = line.replace("\n", "")
    clean_text.append(line)

cleaner_text = []

# gets rid of \ufeff
    
for line in clean_text:
    line = line.replace("\ufeff", "")
    cleaner_text.append(line)
    
    
# splits cleaned text and translates to cat speak then rejoins text   


glue = " "

cat_text_list = []

for line in cleaner_text:
    temp_line = []
    line = line.split(" ")
    for word in line:
        if word in cat_speak_dictionary:
            word = word.replace(word, cat_speak_dictionary[word])
        temp_line.append(word)
    line = glue.join(temp_line)
    cat_text_list.append(line)


# Step 4
# Save the translated text as the "lolcat.txt" file

with open('lolcat.txt', 'w') as f:
    for line in cat_text_list:
        f.write(line)
        f.write("\n")
