import re
def split_string(pattern, string):
        return re.split(pattern, string)
def find_unique_words(sentence):
        return set(sentence.split())