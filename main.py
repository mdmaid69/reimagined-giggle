import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def count_characters(sentence):
        return len(sentence)