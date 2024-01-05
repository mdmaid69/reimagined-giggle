text = "Hello, world!"
print("Words:", len(text.split()))
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()