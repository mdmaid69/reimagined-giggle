import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
from collections import Counter
print(Counter("hello world"))