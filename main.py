import os
def get_file_size(filename):
        return os.path.getsize(filename)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))