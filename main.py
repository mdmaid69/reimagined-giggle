import os
def remove_directory(path):
        os.rmdir(path)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())