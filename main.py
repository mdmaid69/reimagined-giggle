n = 10
print("Square numbers:", [x**2 for x in range(n)])
import shutil
def delete_directory(path):
        shutil.rmtree(path)