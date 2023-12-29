sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import os
def get_environment_variable(var):
        return os.getenv(var)