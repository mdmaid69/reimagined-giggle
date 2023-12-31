def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)