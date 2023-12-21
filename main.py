import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import sklearn.datasets
print(sklearn.datasets.load_iris())