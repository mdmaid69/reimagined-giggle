import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])