import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def calculate_perpetuity(payment, rate):
        return payment / rate