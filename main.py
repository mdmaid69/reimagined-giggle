import sklearn.datasets
print(sklearn.datasets.load_iris())
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable