import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
name = "Python"
print("Hello,", name)