def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)