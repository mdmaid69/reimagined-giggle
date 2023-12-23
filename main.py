import random
def generate_random_choice(choices):
        return random.choice(choices)
def find_unique_words(sentence):
        return set(sentence.split())