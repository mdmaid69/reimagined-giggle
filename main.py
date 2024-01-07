import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def count_characters(sentence):
        return len(sentence)