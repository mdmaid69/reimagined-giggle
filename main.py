import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps