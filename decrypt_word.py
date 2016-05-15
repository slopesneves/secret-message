import shutil
import os

encrypted_word_directory = "encrypted_word"
decrypted_word_directory = "decrypted_word"

if os.path.exists(decrypted_word_directory):
    shutil.rmtree(decrypted_word_directory)
    print(decrypted_word_directory + " successfully cleaned")
        
os.makedirs(decrypted_word_directory)

encrypted_file_names = os.listdir(encrypted_word_directory)
for encrypted_file_name in encrypted_file_names:
    decrypted_file_name = ''.join([letter for letter in encrypted_file_name if not letter.isdigit()])
    shutil.copyfile(encrypted_word_directory + "/" + encrypted_file_name, decrypted_word_directory + "/" + decrypted_file_name)
