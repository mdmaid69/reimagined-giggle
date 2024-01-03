import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())