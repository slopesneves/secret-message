import urllib.request
import string


letters = string.ascii_uppercase
print("Starting to download letter to make secret message")
for letter in letters:
    url = "http://icons.iconarchive.com/icons/mattahan/umicons/128/Letter-" + letter +"-icon.png"
    urllib.request.urlretrieve(url, "letter-image/letter-" + letter + ".jpg")
    print("Success to download " + url)
print("Letters are successfuly downloaded")
