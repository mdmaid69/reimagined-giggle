import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])