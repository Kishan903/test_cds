import random
import string

def add_words(file_name, cdn_value):
    word_to_write = random.randint(0, 50) 
    with open(file_name, "a+") as file:
        for i in range(word_to_write):
            add_cdn = [True, False]
            add_value_string = random.choice(add_cdn)
            string_length = random.randint(0, 20) 
            if add_value_string:    
                file.write(cdn_value)
                file.write(" ")
            else:
                value = ''.join(random.choices(string.ascii_letters, k=string_length))
                file.write(value)
                file.write(" ")
        else:
            file.write("\n")