import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import sklearn.datasets
print(sklearn.datasets.load_iris())