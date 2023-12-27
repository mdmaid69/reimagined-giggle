import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))