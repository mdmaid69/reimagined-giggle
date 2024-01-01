import os
def change_working_directory(path):
        os.chdir(path)
def find_unique_words(sentence):
        return set(sentence.split())