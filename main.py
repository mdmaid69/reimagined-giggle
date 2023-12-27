import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")