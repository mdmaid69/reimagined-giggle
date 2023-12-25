import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True