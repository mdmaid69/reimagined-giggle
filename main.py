import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import sklearn.datasets
print(sklearn.datasets.load_iris())