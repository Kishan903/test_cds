import logging
import os

from utils.add_word import add_words
from utils.count_word import count_words

from django.conf import settings

watcher_log = logging.getLogger("watcher_log")

def count_values():
    w = os.walk(settings.WATCHER_DIR)
    for (dirpath, dirnames, filenames) in w: 
        
        for filename in filenames:
            count = count_words(dirpath, filename, "any")
            if count > 0:
                message = os.path.join(dirpath, filename) + " - " + str(count)
                print("ok")
                watcher_log.info(message)

def add_data_to_file_1():
    value = os.environ.get("DEFAULT_VALUE", "CDS")
    add_words(os.path.join(settings.WATCHER_DIR, "file_1.txt"), value)

def add_data_to_file_2():
    value = os.environ.get("DEFAULT_VALUE", "CDS")
    add_words(os.path.join(settings.WATCHER_DIR, "file_2.txt"), value)