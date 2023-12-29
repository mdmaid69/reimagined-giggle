def is_palindrome(s):
        return s == s[::-1]
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"