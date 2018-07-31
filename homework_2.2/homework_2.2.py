import yaml
import json
from pprint import pprint

# YAML
def get_dishes_yaml():
    dishes_yaml = dict()
    with open('hw2.2_yaml.yaml', encoding='utf8') as f:
        dishes_yaml = yaml.load(f)
        # pprint(dishes)

    return dishes_yaml

# JSON
def get_dishes_json():
    dishes_json = dict()
    with open('hw2.2_json.json', encoding='utf8') as f:
        dishes_json = json.load(f)
        # pprint(dishes_json)

    return dishes_json

def get_shop_list_by_dishes(dishes, person_count, what_parcing):
  shop_list = {}
  for dish in dishes:
    for ingridient in what_parcing[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
# for shop_list_item in shop_list.values(): #1 вариант вывода
#   print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))
  for shop_list_item in shop_list.values(): #арги, почитать
    print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))

def create_shop_list():
  person_count = int(input('Введите количество человек'))
  dishes = input('Введите название блюд').split(', ')
  what_parcing = input('Что будем разбирать? (YAML или JSON)')
  if what_parcing == "yaml":
      what_parcing = get_dishes_yaml()
  if what_parcing == "json":
      what_parcing = get_dishes_json()
  shop_list = get_shop_list_by_dishes(dishes, person_count, what_parcing)
  print_shop_list(shop_list)

create_shop_list()