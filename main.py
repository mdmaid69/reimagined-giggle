import sklearn.datasets
print(sklearn.datasets.load_iris())
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)