#1
# s = "How are you? Eh, ok. Low or Lower? Ohhh."
#
# def upper_char(s):
#     w = []
#     for char in s:
#         if char.isupper():
#             w.append(char)
#     return w
#
# print(upper_char(s))

#2
# number = [1,2,3,4,5]
#
# def even_index_sm(number):
#         sum_even = 0
#         for i in range(0, len(number), 2):
#                 sum_even += number[i]
#                 multiply_sum = sum_even * number[-1]
#         return multiply_sum
#
# print(even_index_sm(number))

#3
# s1 = ". awe'awe, wae,spdmf. skdf"
#
# def first_word_string(s1):
#     first_word = lambda s1: s1.replace('.', '').replace(',', '').strip().split(' ')[0]
#     return first_word(s1)
#
# print(first_word_string(s1))

#4
# s2 = 'qwe ppp lll ewу'
#
# def swap_first_last(s2):
#     lst = list(s2)
#     lst[0], lst[-1] = lst[-1], lst[0]
#     s2 = ''.join(lst)
#     return s2
#
# print(swap_first_last(s2))

#5
# lst_tuple  = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
#
# def conver_to_srting(lst_tuple):
#     s = ''.join(lst_tuple)
#     return s
#
# print(conver_to_srting(lst_tuple))
