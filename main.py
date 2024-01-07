import sys
def add_to_python_path(path):
        sys.path.append(path)
def find_unique_words(sentence):
        return set(sentence.split())