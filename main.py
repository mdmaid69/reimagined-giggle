import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])