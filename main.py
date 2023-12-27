import os
def get_current_working_directory():
        return os.getcwd()
def count_words(sentence):
        return len(sentence.split())