import os
def change_working_directory(path):
        os.chdir(path)
def count_words(sentence):
        return len(sentence.split())