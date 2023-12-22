import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import tensorflow as tf
print(tf.__version__)