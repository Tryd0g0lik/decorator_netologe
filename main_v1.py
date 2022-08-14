from habr.get_page import craper_word
from habr.decorate import decor_word
from habr.decorate import decor_pars
from habr.get_page import search_page
from habr.get_page import keyword
import datetime

if __name__ == ("__main__"):
  log = {}

  url = "https://habr.com/ru/search/"

  fmt = "%Y-%m-%d %H:%M:%S"
  time_start = datetime.datetime.now().strftime(fmt)
  name_ = craper_word.__name__
  fun_object = craper_word




  time_start = datetime.datetime.now().strftime(fmt)
  name_ = decor_word(fun_object).__name__
  list_phrase = decor_word(fun_object)

  list_, words = list_phrase()

  time_start = datetime.datetime.now().strftime(fmt)
  name_ = decor_pars(search_page).__name__
  fun_get_prser = decor_pars(search_page)

  response = fun_get_prser(url, list_)
  logirovanie = {}
  log["keyword"] = words
  log["time"] = time_start
  log["function-name"] = name_
  log["response"] = response[1]

  try:
    file =  open("files/log.txt", "xwt", encoding="utf=8")
    file.write(str(log))

  except Exception:
    file = open("files/log.txt", "wt", encoding="utf=8")
    file.write(str(log))
  finally:
    file.close()
