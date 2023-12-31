import logging
def setup_logging(level):
        logging.basicConfig(level=level)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))