import os
def remove_directory(path):
        os.rmdir(path)
def find_unique_words(sentence):
        return set(sentence.split())