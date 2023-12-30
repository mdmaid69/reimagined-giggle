import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import sklearn.datasets
print(sklearn.datasets.load_iris())