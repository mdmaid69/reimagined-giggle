  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import logging
def log_message(message):
        logging.info(message)