import platform
def get_os_info():
        return platform.uname()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))