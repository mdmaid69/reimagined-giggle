import logging
def log_message(message):
        logging.info(message)
def calculate_roi(gain, cost):
        return (gain - cost) / cost