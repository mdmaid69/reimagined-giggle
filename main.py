import os
def get_current_working_directory():
        return os.getcwd()
def find_unique_words(sentence):
        return set(sentence.split())