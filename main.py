import platform
def get_python_version():
        return platform.python_version()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))