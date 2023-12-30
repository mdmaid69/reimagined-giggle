import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
for i in range(5):
        print(i)