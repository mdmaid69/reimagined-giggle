import shutil
def delete_directory(path):
        shutil.rmtree(path)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])