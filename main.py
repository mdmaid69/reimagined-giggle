list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread