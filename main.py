import getpass
def get_username():
        return getpass.getuser()
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time