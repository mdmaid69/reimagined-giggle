import random
def generate_random_choice(choices):
        return random.choice(choices)
def is_palindrome(s):
        return s == s[::-1]