import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal