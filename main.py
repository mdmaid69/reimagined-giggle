sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)