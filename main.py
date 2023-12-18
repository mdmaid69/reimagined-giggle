import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import sklearn.datasets
print(sklearn.datasets.load_iris())