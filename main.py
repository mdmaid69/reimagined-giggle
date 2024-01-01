import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
x = 10
y = 20
print("Sum:", x + y)