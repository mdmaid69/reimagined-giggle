import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()