import sys
def print_python_version():
        return sys.version
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())