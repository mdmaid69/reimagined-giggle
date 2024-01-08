  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())