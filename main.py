import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))