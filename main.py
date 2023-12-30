import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
text = "Hello, world!"
print("Characters:", len(text))