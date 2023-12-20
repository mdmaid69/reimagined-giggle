import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])