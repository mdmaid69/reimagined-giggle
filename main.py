import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))