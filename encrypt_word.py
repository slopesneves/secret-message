import os;
import shutil;
import random

renamed_word_file_directory = "renamed_user_word"
encrypted_word_file_directory = "encrypted_word"
file_names = os.listdir(renamed_word_file_directory)

values_to_encrypt = []
value_to_encrypt = 0
max_encrypt_value = 10

while value_to_encrypt < max_encrypt_value:
    values_to_encrypt.append(str(value_to_encrypt))
    value_to_encrypt = value_to_encrypt + 1

print(values_to_encrypt)

if os.path.exists(encrypted_word_file_directory):
    shutil.rmtree(encrypted_word_file_directory)
    print(encrypted_word_file_directory + " successfully cleaned")
        
os.makedirs(encrypted_word_file_directory)

for file_name in file_names:
    encrypted_name = list(file_name.rstrip(".jpg"))

    encryption_times = random.randrange(len(encrypted_name),len(encrypted_name) * 2)
    encryption_counter = 0
    while encryption_counter < encryption_times:
        range_to_add_value = random.randrange(0,len(encrypted_name))
        value_to_add = str(random.randrange(0,len(values_to_encrypt)))
        encrypted_name.insert(range_to_add_value, value_to_add)
        encryption_counter = encryption_counter + 1

    origin_file_name = renamed_word_file_directory + "/" + file_name
    encrypted_file_name = encrypted_word_file_directory + "/" + ''.join(encrypted_name) + ".jpg"
    
    shutil.copyfile(origin_file_name, encrypted_file_name)

    
    print("Encryption from " + origin_file_name + " to " + encrypted_file_name)
    
