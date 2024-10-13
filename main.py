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
print(f'cook_book = {cook_book}')

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
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

#Задача_3
