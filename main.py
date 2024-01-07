import os
def remove_directory(path):
        os.rmdir(path)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))