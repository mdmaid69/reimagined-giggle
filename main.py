def find_unique_words(sentence):
        return set(sentence.split())
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)