import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
x = 10
y = 20
print("Sum:", x + y)