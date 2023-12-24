def count_words(sentence):
        return len(sentence.split())
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)