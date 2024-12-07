#my_dict = {'Pavel': 1983, 'Max': 2000}
#print('Dict:',my_dict)
#print('Existing value:',my_dict['Pavel'])  # Выведите на экран одно значение по существующему ключу
#print('Not existing value:',my_dict.get('Kaila')) #одно по отсутствующему из словаря my_dict без ошибки
#my_dict.update({'Mihail': 2005,
 #               'Igor': 2010})
#print(my_dict)
#a = my_dict.pop('Max')  #Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экра
#print('Deleted value:',a)
#print('Modified dictionary:',my_dict)

my_set_= {1, 'Apple', 42.314, 1, 2, 5, 2234, (4,3,4,3,4)}
set_ = [1,1,24,4,4,4]
my_set_ = set(my_set_)
print(my_set_)
print(my_set_.add(100))  #Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
print(my_set_.add(200))  #Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
print(my_set_)

print(my_set_.remove(100))   #  - Удалите один любой элемент из множества my_set.
print('Modified set:',my_set_)


