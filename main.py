import platform
def get_python_version():
        return platform.python_version()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))