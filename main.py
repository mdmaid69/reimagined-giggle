import random
def generate_random_number(start, end):
        return random.randint(start, end)
def is_palindrome(s):
        return s == s[::-1]