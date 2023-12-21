import sys
def exit_program():
        sys.exit()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())