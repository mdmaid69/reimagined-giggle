import getpass
def get_username():
        return getpass.getuser()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps