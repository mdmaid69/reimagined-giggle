import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def count_words(sentence):
        return len(sentence.split())