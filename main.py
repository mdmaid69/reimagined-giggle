import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])