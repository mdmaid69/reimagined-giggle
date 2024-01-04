import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)