import os
def list_files_in_directory(path):
        return os.listdir(path)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))