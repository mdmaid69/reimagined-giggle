def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)