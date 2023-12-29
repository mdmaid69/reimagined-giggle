import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)