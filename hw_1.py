import random
#1
def its_dict(keys):
    d = {key: key * key for key in keys}
    print(d)

its_dict([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#2
def even_list(a):
    for i in range (1,101):
        if i % 2 == 0:
            a.append(i)
    return a
print(even_list([]))

#3
def consonants_to_vowels(str):
    endstr = []
    for char in str:
        if char in 'bcdfghjklmnpqrstvwxyz':
            endstr.append(random.choice('aeiou'))
        else:
            endstr.append(char)
    str = ''.join(endstr)
    return str

print(consonants_to_vowels('abbccdd'))

#4
def work_list(number):
    myset = set(number)
    max_num = list(myset)
    max_num.sort(reverse=True)
    three_max_num = max_num[0:3]
    index_to_max = number.index(min(number))
    number.reverse()
    return myset, three_max_num, index_to_max, number
print(work_list([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))

#5
dict_one = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
dict_two = { 'a': 6, 'b': 7, 'z': 20, 'x': 40 }

def two_kay(dict_one, dict_two):
    lst_key = []
    for key1 in dict_one.keys():
        for key2 in dict_two.keys():
            if key1 == key2:
                lst_key.append(key1)
    return lst_key

print(two_kay(dict_one,dict_two))
