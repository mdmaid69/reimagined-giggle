import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))