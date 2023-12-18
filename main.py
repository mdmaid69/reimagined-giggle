import platform
def get_os_info():
        return platform.uname()
import sklearn.datasets
print(sklearn.datasets.load_iris())