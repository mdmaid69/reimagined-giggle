def is_palindrome(s):
        return s == s[::-1]
import random
def generate_random_sample(population, k):
        return random.sample(population, k)