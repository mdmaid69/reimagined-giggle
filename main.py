import shutil
def move_file(src, dst):
        shutil.move(src, dst)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])