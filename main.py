import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import sklearn.datasets
print(sklearn.datasets.load_iris())