import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
from collections import Counter
print(Counter("hello world"))