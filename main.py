import random
def generate_random_choice(choices):
        return random.choice(choices)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())