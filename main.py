import sklearn.datasets
print(sklearn.datasets.load_iris())
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())