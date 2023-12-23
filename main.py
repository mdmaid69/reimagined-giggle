import re
print(re.match("h.*o", "hello world"))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())