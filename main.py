import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import sklearn.datasets
print(sklearn.datasets.load_iris())