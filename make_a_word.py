import shutil
import os


user_word_directory = "user-word/"
letter_position = 1

if os.path.exists(user_word_directory):
    shutil.rmtree(user_word_directory)
    print(user_word_directory + " successfully cleaned")
        
os.makedirs(user_word_directory)
        

user_word = input("Enter a word : ")
print("You write " + user_word)

print("Starting to copy image in " + user_word_directory)
for letter in user_word:
    shutil.copy("letter-image/letter-" + letter + ".jpg", user_word_directory + str(letter_position) + ".jpg")
    print("Success to copy " + letter)
    letter_position = letter_position + 1
