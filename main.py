import os
def get_current_working_directory():
        return os.getcwd()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))