  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def is_palindrome(s):
        return s == s[::-1]