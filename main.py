import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import sklearn.datasets
print(sklearn.datasets.load_iris())