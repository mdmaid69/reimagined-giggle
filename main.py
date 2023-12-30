import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
for i in range(10): print(i)