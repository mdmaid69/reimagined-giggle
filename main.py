text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())