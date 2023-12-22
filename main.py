import getpass
def get_username():
        return getpass.getuser()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))