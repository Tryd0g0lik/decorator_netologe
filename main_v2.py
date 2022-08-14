from habr_v2 import get_page




if __name__ == ("__main__"):
  url = "https://habr.com/ru/search/"

  list_, words = get_page.craper_word()
  get_page.search_page(url, words)