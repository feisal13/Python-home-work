from collections import Counter
from pprint import pprint
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

#1.1
def sort_age(data):
    return sorted(data, key=lambda k: k['age'])

pprint(sort_age(data))

#1.2
def sort_city(data):
    result = {}
    for i in data:
        lst = [{'name': i['name'], 'age': i['age']}]
        result[i['city']] = lst
        return result

pprint(sort_city(data))

#2
def most_frequent(list_var):
    count_string = Counter(list_var)
    max_string = max(count_string)
    return max_string
print(most_frequent(['a', 'a', 'bi', 'bi', 'bi']))

#3
def multiply_number(number):
    b = str(number)
    a = list(b)
    c = 1
    for i in a:
        if i != '0':
            c *= int(i)
        else:
            del(i)
    return c
print(multiply_number(123405))

#4
def some_function(array, n):
    if n < len(array):
        return array[n] ** n
    else:
        return -1

print(some_function([1,2,4,5,7], 3))


#5
def three_word(s):
    s_list = s.split()
    word = 0
    for i in s_list:
        if i.isalpha():
            word += 1
            if word == 3:
                return True
        else:
            word = 0
    return False
print(three_word("hello 1 one two three 15 world"))

