import sklearn.datasets
print(sklearn.datasets.load_iris())
import array
def get_bytes_from_array(array):
        return array.tobytes()