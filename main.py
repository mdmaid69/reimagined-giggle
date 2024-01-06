import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)