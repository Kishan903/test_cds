from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import logging
import random
import os


watcher_log = logging.getLogger("watcher_log")

# Create your views here.
def file_1_writer(request):
    with open(os.path.join(settings.WATCHER_DIR, "file_1.txt"), "a+") as file1:
        # Writing data to a file
        file1.write("Hello \n")
        # file1.writelines(L)
    return HttpResponse("hello")

