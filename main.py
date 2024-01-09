list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()