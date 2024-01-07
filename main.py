import random
print(random.randint(0, 100))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())