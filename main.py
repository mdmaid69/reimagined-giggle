import sklearn.datasets
print(sklearn.datasets.load_iris())
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a