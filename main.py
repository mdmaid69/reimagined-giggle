import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def count_characters(sentence):
        return len(sentence)