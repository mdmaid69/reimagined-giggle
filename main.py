import re
print(re.match("h.*o", "hello world"))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)