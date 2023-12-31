numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import shutil
def delete_directory(path):
        shutil.rmtree(path)