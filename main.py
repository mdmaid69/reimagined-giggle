import os
def get_current_working_directory():
        return os.getcwd()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())