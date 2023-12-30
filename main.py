import os
def list_files_in_directory(path):
        return os.listdir(path)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())