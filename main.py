import getpass
def get_username():
        return getpass.getuser()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))