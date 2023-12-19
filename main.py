def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import getpass
def get_username():
        return getpass.getuser()