import tensorflow as tf
print(tf.__version__)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)