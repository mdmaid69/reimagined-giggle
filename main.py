import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def find_unique_words(sentence):
        return set(sentence.split())