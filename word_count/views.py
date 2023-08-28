from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import logging
import random
import os

from utils import add_word
import os
watcher_log = logging.getLogger("watcher_log")

# Create your views here.
def test(request):
    add_word("file1.txt", os.environ.get("word", "CDN"))
    
    # file_names = ["file_1.txt", "file_2.txt"] 
    # file_name = random.choice(file_names)
    # with open(os.path.join(settings.WATCHER_DIR, file_name), "w") as file1:
    #     # Writing data to a file
    #     file1.write("Hello \n")
        # file1.writelines(L)
    return HttpResponse("hello")    
