import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def count_words(sentence):
        return len(sentence.split())