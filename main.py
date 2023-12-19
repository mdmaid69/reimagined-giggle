import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import re
print(re.match("h.*o", "hello world"))