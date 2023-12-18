import getpass
def get_username():
        return getpass.getuser()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)