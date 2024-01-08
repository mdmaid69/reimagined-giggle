import datetime
print(datetime.datetime.now())
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)