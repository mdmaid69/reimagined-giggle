import platform
def get_os_info():
        return platform.uname()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))