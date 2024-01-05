import os
def list_files_in_directory(path):
        return os.listdir(path)
def count_words(sentence):
        return len(sentence.split())