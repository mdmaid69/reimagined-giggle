import datetime
def get_current_date():
        return datetime.date.today()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)