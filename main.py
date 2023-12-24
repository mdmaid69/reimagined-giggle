import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def find_unique_words(sentence):
        return set(sentence.split())