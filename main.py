import sklearn.datasets
print(sklearn.datasets.load_iris())
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)