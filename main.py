import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread