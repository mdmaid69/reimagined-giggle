import random
def generate_random_number(start, end):
        return random.randint(start, end)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))