n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()