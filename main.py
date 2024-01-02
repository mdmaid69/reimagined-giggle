import getpass
def get_username():
        return getpass.getuser()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)