n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()