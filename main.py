def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()