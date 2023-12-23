import os
def change_working_directory(path):
        os.chdir(path)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())