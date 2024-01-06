import time
print(time.time())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())