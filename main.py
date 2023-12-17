import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))