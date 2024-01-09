import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def count_characters(sentence):
        return len(sentence)