n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread