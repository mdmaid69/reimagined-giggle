sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)