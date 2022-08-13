import bs4
import re
import requests
import sys



def sapghetti(fun):

  def new_scraper(*args):
    pass
    return

  return new_scraper


def craper_word():
  word_of_sentence = input("Enter: ")
  return word_of_sentence

def keyword(word_of_sentence):
  return word_of_sentence




def search_page(url_, params_ = None, header_=None, data_ = None):
  try:
    response = requests.get(url_, params=params_, headers=header_, data=data_, timeout=(2, 7)).text

  except Exception as er:
    print(sys.exc_info(), "and", er)


  return response

