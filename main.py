import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2