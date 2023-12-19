import random
def generate_random_choice(choices):
        return random.choice(choices)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])