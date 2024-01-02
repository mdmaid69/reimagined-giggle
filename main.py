import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)