import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])