import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
i = 0
while i < 5:
        print(i)
        i += 1