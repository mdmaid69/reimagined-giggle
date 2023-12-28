import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b