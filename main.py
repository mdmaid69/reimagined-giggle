import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])