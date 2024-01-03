import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def find_unique_words(sentence):
        return set(sentence.split())