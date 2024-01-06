import random
def generate_random_choice(choices):
        return random.choice(choices)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))