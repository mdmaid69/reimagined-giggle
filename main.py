import random
def generate_random_sample(population, k):
        return random.sample(population, k)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))