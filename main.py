import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def convert_to_binary(n):
        return bin(n)