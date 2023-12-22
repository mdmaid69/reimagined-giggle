def find_unique_words(sentence):
        return set(sentence.split())
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()