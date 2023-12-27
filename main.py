import sys
def add_to_python_path(path):
        sys.path.append(path)
def count_words(sentence):
        return len(sentence.split())