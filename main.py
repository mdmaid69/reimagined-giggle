import random
def generate_random_sample(population, k):
        return random.sample(population, k)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])