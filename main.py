import random
def generate_random_number(start, end):
        return random.randint(start, end)
def find_unique_words(sentence):
        return set(sentence.split())