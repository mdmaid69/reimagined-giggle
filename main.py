import shutil
def delete_directory(path):
        shutil.rmtree(path)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])