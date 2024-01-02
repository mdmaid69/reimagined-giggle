import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
i = 0
while i < 5:
        print(i)
        i += 1