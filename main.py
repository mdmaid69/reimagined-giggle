import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def count_words(sentence):
        return len(sentence.split())