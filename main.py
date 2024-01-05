import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import getpass
def get_username():
        return getpass.getuser()