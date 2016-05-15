import urllib.request
import string
import os
import shutil


letter_image_directory = "letter-image"
if os.path.exists(letter_image_directory):
    shutil.rmtree(letter_image_directory)
    print(letter_image_directory + " successfully cleaned")
        
os.makedirs(letter_image_directory)
letters = string.ascii_uppercase
print("Starting to download letter to make secret message")
for letter in letters:
    url = "http://icons.iconarchive.com/icons/mattahan/umicons/128/Letter-" + letter +"-icon.png"
    urllib.request.urlretrieve(url, letter_image_directory +"/letter-" + letter + ".jpg")
    print("Success to download " + url)
print("Letters are successfuly downloaded")
