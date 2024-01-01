import sklearn.datasets
print(sklearn.datasets.load_iris())
import getpass
def get_username():
        return getpass.getuser()