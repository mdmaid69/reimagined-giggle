import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
i = 0
while i < 5:
        print(i)
        i += 1