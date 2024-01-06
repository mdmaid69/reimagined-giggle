sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import os
def get_environment_variable(var):
        return os.getenv(var)