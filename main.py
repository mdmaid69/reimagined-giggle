import sklearn.datasets
print(sklearn.datasets.load_iris())
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()