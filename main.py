import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import itertools
print(list(itertools.permutations([1, 2, 3])))