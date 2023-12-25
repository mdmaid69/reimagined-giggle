import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())