import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def find_unique_words(sentence):
        return set(sentence.split())