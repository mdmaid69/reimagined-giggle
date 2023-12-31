import sys
def print_python_version():
        print(sys.version)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())