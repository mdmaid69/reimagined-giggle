import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def count_words(sentence):
        return len(sentence.split())