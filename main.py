import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import sklearn.datasets
print(sklearn.datasets.load_iris())