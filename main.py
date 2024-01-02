import shutil
def delete_directory(path):
        shutil.rmtree(path)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])