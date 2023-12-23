import shutil
def move_file(src, dst):
        shutil.move(src, dst)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))