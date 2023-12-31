def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"