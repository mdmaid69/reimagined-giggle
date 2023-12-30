def count_words(sentence):
        return len(sentence.split())
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)