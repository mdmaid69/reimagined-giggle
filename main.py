import time
def get_time_since_epoch():
        return time.time()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])