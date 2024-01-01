import os
def list_files_in_directory(path):
        return os.listdir(path)
def find_unique_words(sentence):
        return set(sentence.split())