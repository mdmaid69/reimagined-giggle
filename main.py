text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()