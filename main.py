import random
def generate_random_number(start, end):
        return random.randint(start, end)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())