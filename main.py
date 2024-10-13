#Задача_1
cook_book = {}

with open('recipe book.txt', 'rt', encoding='utf-8') as file:
	for l in file:
		department_name = l.strip()
		dictik = []
		listik = {}
		employees_count = file.readline()
		for i in range(int(employees_count)):
			emp = file.readline()
			ingredient_name, quantity, measure  = emp.strip().split(' | ')
			dictik.append({'ingredient_name': ingredient_name,
                                     'quantity': int(quantity),
                                     'measure': measure})
			dep = {department_name: dictik}
		blank_line = file.readline()
		cook_book.update(dep)
#print(f'cook_book = {cook_book}')

#Задача_2
def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                   result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity']) * int(person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
#get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

#Задача_3
import os.path
import os

def acounting(file:str) -> int:
    return sum(1 for _ in open('1.txt', 'rt', encoding='utf-8'))

def rewriting(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r',encoding='utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()
        
file_for_writing = os.path.abspath('Users\Алексей\OneDrive\Рабочий стол\file_from_list\1.txt')
base_path = os.getcwd()
location = os.path.abspath('Users\Алексей\OneDrive\Рабочий стол\file_from_list')
rewriting(file_for_writing, base_path, location) 