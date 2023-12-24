  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import logging
def log_message(message):
        logging.info(message)