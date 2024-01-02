n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()