import bs4
import re
import requests
import sys
import habr_v2.decorate as dec

@dec.decor_word
def craper_word():
  word_of_sentence = input("Enter: ")
  return word_of_sentence

def keyword(word_of_sentence):
  return word_of_sentence



@dec.decor_pars
def search_page(url_, params_ = None, header_=None, data_ = None):
  try:
    response = requests.get(url_, params=params_, headers=header_, data=data_, timeout=(2, 7)).text

  except Exception as er:
    print(sys.exc_info(), "and", er)


  return response

