  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def count_words(sentence):
        return len(sentence.split())