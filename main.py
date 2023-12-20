import getpass
def get_username():
        return getpass.getuser()
def greet(name):
        print(f"Hello, {name}!")