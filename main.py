import os
def remove_directory(path):
        os.rmdir(path)
def count_words(sentence):
        return len(sentence.split())