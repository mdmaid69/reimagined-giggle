import array
def get_array_as_bytearray(array):
        return bytearray(array)
import sklearn.datasets
print(sklearn.datasets.load_iris())