import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time