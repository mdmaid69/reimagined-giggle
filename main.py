import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time