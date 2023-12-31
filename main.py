import random
def roll_die():
        return random.randint(1, 6)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])