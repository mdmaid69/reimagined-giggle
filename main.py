import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])