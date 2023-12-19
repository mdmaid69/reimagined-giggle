sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import os
def change_working_directory(path):
        os.chdir(path)