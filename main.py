import logging
def log_message(message):
        logging.info(message)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))