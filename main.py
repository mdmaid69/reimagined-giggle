sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)