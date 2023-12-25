import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))