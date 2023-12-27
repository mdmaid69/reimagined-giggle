import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import re
print(re.match("h.*o", "hello world"))