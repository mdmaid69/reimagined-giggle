import random
print(random.randint(0, 100))
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()