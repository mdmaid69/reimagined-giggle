sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import os
def remove_directory(path):
        os.rmdir(path)