def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import random
def roll_die():
        return random.randint(1, 6)