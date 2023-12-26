import shutil
def delete_directory(path):
        shutil.rmtree(path)
n = 10
print("Powers of 2:", [2**x for x in range(n)])