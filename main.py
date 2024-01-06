import getpass
def get_username():
        return getpass.getuser()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)