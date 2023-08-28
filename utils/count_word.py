import os
import re


def count_words(dirpath, filename, word):
    initial_count = 0
    with open(os.path.join(dirpath, filename)) as file:
        for line in file:
            x = re.findall(f" {word}", line)
            initial_count += len(x)
    return initial_count