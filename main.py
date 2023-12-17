import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
i = 0
while i < 5:
        print(i)
        i += 1