import sklearn.datasets
print(sklearn.datasets.load_iris())
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")