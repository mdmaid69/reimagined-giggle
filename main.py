import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))