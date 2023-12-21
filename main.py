import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def find_unique_words(sentence):
        return set(sentence.split())