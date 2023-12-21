def calculate_volume(length, width, height):
        return length * width * height
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()