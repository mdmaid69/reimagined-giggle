import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)