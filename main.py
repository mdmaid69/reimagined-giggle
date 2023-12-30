import re
def split_string(pattern, string):
        return re.split(pattern, string)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())