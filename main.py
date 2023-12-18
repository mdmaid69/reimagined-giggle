import random
def generate_random_choice(choices):
        return random.choice(choices)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))