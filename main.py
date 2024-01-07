import getpass
def get_username():
        return getpass.getuser()
import sklearn.datasets
print(sklearn.datasets.load_iris())