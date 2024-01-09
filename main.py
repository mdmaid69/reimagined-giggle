import sklearn.datasets
print(sklearn.datasets.load_iris())
import platform
def get_os_info():
        return platform.uname()