import random
def generate_random_number(start, end):
        return random.randint(start, end)
import sklearn.datasets
print(sklearn.datasets.load_iris())