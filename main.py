import re
print(re.match("h.*o", "hello world"))
import shutil
def delete_directory(path):
        shutil.rmtree(path)