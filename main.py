def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)