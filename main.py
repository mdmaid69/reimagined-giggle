import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import sklearn.datasets
print(sklearn.datasets.load_iris())