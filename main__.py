import random
import time


def my_generator():
  # этот код выполнится на входе в цикл for item in my_generator()

  print('Цикл начался')

  while True:

    if random.randint(1, 10) == 1:
      # условие выхода из цикла
      print('выход из цикла')

      break

    print('-' * 20)
    print('Новая итерация')

    result = time.time()

    # result подставится в item
    print(f'{result} -> item')

    yield result


for item in my_generator():
  print(item)



