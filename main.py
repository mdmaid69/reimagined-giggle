import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)