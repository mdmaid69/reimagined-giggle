import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def count_characters(sentence):
        return len(sentence)