import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])