sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)