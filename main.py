from pprint import pprint

# Задача №1

with open('recipe_list.txt', encoding='utf-8') as file:
    cook_book = {}
    while True:
        recipe_name = file.readline().strip()
        if recipe_name == '':
            break
        ingredients_count = int(file.readline())
        ingredients = []
        for p in range(ingredients_count):
            recipe = file.readline().strip().split(' | ')
            product, quantity, measure = recipe
            ingredients.append({'ingredient_name': product, 'quantity': int(quantity), 'measure': measure})
        file.readline()
        cook_book[recipe_name] = ingredients

pprint(cook_book)

# Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))

# Задача №3
import os

# Объединить 2 файла в один с помощью os.path.join
def collapse_files(file1, file2):
    with open(file1, encoding='utf-8') as f1:
        with open(file2, encoding='utf-8') as f2:
            with open('collapse.txt', 'w', encoding='utf-8') as f3:
                #Добавляем имя файла в список
                f1_text = [f1.name]
                for item in f1.readlines():
                    f1_text.append(item)
                f1_len_str = str(len(f1_text) - 1)
                f1_text.insert(1, f1_len_str)
                f2_text = [f2.name]
                for item in f2.readlines():
                    f2_text.append(item)
                f2_len_str = str(len(f2_text) - 1)
                f2_text.insert(1, f2_len_str)
                #Убираем перенос строки
                f1_text = [line.rstrip() for line in f1_text]
                f2_text = [line.rstrip() for line in f2_text]
                #Записываем в файл
                if len(f1_text) < len(f2_text):
                    for item in f1_text:
                        f3.write(item + '\n')
                    for item in f2_text:
                        f3.write(item + '\n')
                else:
                    for item in f2_text:
                        f3.write(item + '\n')
                    for item in f1_text:
                        f3.write(item + '\n')

collapse_files('1.txt', '2.txt')