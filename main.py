import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import sklearn.datasets
print(sklearn.datasets.load_iris())