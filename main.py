import sys
def add_to_python_path(path):
        sys.path.append(path)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])