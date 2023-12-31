def count_words(sentence):
        return len(sentence.split())
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()