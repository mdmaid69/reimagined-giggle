def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()