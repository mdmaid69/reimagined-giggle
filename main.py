import getpass
def get_username():
        return getpass.getuser()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time