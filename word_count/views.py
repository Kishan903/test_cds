from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import logging
import os
from django.conf import settings
from utils.add_word import add_words
from utils.count_word import count_words

watcher_log = logging.getLogger("watcher_log")

# Create your views here.
def test(request):
    w = os.walk(settings.WATCHER_DIR)
    for (dirpath, dirnames, filenames) in w: 
        
        for filename in filenames:
            count = count_words(dirpath, filename, "CDS")
            print(count)

    return HttpResponse("hello")