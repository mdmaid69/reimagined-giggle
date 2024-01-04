import sklearn.datasets
print(sklearn.datasets.load_iris())
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list