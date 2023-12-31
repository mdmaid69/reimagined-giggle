import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b