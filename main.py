import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)