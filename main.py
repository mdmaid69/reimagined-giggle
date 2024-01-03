def count_words(sentence):
        return len(sentence.split())
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)