def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import getpass
def get_username():
        return getpass.getuser()