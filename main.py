import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)