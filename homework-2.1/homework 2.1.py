from pprint import pprint

def get_dishes():
    dishes_all = dict()
    with open('666.txt', 'r') as f:
        for line in f:
            dishes_value = list()
            dishes = line.strip()
            ingridient_count = int(f.readline().strip())
            for _ in range(ingridient_count):  # _ означает, что переменную мы не будем использовать
                ingredient = f.readline().strip().split(" | ")
                i = {"ingridient_name": ingredient[0], "quantity": int(ingredient[1]), "measure": ingredient[2]}
                dishes_value.append(i)
            f.readline()
            dishes_all.update({dishes: dishes_value})

    return dishes_all

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    dishes_all = get_dishes() #сохраняем словарь из функции чтобы не обращаться к нему больше (уменьшение времени выполнения программы)
    for dish in dishes:
        for ingridient in dishes_all[dish]:
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
    dishes = input('Введите название блюд в расчете на одного человека').split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()