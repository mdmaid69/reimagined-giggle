import tensorflow as tf
print(tf.__version__)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)