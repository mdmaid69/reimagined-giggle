import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))