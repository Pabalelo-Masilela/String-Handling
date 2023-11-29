# Pseudocode 1
# Create variable for string "Hello word"
# Lower case the whole string
# Create an empty string that wll be the starting point of the new built string
# Use a for loop to loop with the following conditions:
    # begin index at 0 
    # For each even number index - capitalize the character and add to build of new string
    # else leave character as is and add to build of new string
    #increase count by 1 for index each time.
# Print the final fully altered string

# Pseudocode 2
# Create a variable  for string " I am learning to code"
# lower case all the characters
# split the string into seprate words as a list
# Use a for loop to from 0  with the following conditions:
    # for each even number index -- upper case the word
    # else leave the word as lower case
    # increase count by 1 for index each time

# Join the altered charecters into a new string
# Print the new string

character_string = "Hello World"
character_string = character_string.lower()
enumarated_character_string = enumerate(character_string)
new_character_string = " "
# print(list(enumarated_character_string)) - used to test enumarate function 
character_string_list = list(character_string)
print(character_string_list)

i = 0

for char in character_string_list:
    if i % 2 == 0:
        new_character_string += char.upper()
    else:
        new_character_string += char
    i += 1
print(new_character_string)
# The following lines are extra code for a second method I wanted to explore.
print("...................")
for index, character in enumarated_character_string:
    if index % 2 == 0:
        new_character_string += character.upper()
    else:
        new_character_string += character
# print(new_character_string)
print(",,,,,,,,,,,,,,,,,,")

word_string = "I am learning to code"
word_string_split = word_string.split()
print(word_string_split)
new_word_string = " "
for word in word_string_split:
    if i % 2 == 0:
        new_word_string += word.upper()
    else:
        new_word_string += word.lower()
    new_word_string += " "    
    i += 1
print(new_word_string)
