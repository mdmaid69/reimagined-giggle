def count_words(sentence):
        return len(sentence.split())
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)