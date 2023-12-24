import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)