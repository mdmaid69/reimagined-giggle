def find_unique_words(sentence):
        return set(sentence.split())
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)