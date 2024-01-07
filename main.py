import logging
def log_message(message):
        logging.info(message)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)