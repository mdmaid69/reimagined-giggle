import platform
def get_python_version():
        return platform.python_version()
import sklearn.datasets
print(sklearn.datasets.load_iris())