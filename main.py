from collections import Counter
print(Counter("hello world"))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()