import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])