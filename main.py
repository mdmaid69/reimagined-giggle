sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)