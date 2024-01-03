import getpass
def get_username():
        return getpass.getuser()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time