import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def greet(name):
        print(f"Hello, {name}!")