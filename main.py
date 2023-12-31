import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def count_words(sentence):
        return len(sentence.split())