import os
def get_file_size(filename):
        return os.path.getsize(filename)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())