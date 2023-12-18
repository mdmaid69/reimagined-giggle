import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def count_characters(sentence):
        return len(sentence)