import array
import os
import random
import shutil

print("Loading cities")
cities_file = open("france-cities.txt", "r")

cities = cities_file.readlines()

print("Success to load cities")

cities_file.close()

file_letters = os.listdir("user-word")

loaded_cities = []

cities_to_use = len(file_letters)

loaded_cities_counter = 0

print(str(cities_to_use) + " will be use")

while loaded_cities_counter < cities_to_use:
    loaded_city = random.choice(cities)
    loaded_cities.append(loaded_city.strip())
    cities.remove(loaded_city)
    loaded_cities_counter = loaded_cities_counter + 1

loaded_cities.sort()

print("Success to load the following cities : " + str(loaded_cities))

loaded_cities_counter = 0

renamed_user_word_directory = "renamed_user_word/"
user_word_directory = "user-word/"

print("Cleaning renamed user word directory")
if os.path.exists(renamed_user_word_directory):
    shutil.rmtree(renamed_user_word_directory)
    print(renamed_user_word_directory + " successfully cleaned")

os.makedirs(renamed_user_word_directory)

for file_letter in file_letters:
    shutil.copyfile(user_word_directory + file_letter, renamed_user_word_directory + loaded_cities[loaded_cities_counter] + ".jpg")
    loaded_cities_counter = loaded_cities_counter + 1
