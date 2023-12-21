import random
def generate_random_sample(population, k):
        return random.sample(population, k)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))