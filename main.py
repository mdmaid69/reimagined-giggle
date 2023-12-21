import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())