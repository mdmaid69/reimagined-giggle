import time
def get_current_time():
        return time.ctime()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])