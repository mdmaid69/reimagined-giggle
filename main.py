import getpass
def get_username():
        return getpass.getuser()
def calculate_roi(gain, cost):
        return (gain - cost) / cost