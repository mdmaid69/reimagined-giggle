import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)