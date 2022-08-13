import bs4

# from get_page import craper_word
# from get_page import search_page
import sys


def decor_word(fun):

  def wrapper():
    print("""Enter one word or phrase
    Can inter to more one phrases. 
    Each phrase is through symbol ',' with space""")


    words = fun();
    words_list = str(words).strip().split(", ")
    print("word_list", sys.getsizeof(words_list))

    list_var = []
    for row in (phrase for phrase in words_list):
      row = (row) #[ :-1]
      list_var.append(row)
    print("list_var", sys.getsizeof(list_var))

    return list_var, words

  return wrapper



def decor_pars(fun):
  def get_parser(url, words):



    for word in words:
      word = str(word).strip().lower()
      params = {"q" : word, 'target_type' : 'posts', 'order' : 'relevance'}
      result = fun(url, params_=params)

      try:
        soup = bs4.BeautifulSoup(result, features='html.parser')

        html_soup = soup.find_all("div", class_="tm-article-snippet")

      except Exception:
        print(sys.exc_info())

      try:
        for html_elemet in html_soup:
          htmml_h2 = html_elemet.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").text

          html_time_div = html_elemet.find("div", class_="tm-article-snippet__meta")
          html_time_span = html_time_div.find("span", class_="tm-article-snippet__datetime-published")
          text_datatima = html_time_span.find("time").text

          response = ("""
          Название поста: %s
          Время публикации: %s  
          """%(htmml_h2, text_datatima))
          print(response)
      except Exception:
        print(sys.exc_info() )


    return (result, response)

  return get_parser

# декоратор, итераторы, iterator, магические функции

