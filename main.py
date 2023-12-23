import logging
def log_message(message):
        logging.info(message)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)