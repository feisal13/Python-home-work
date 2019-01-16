#1
# a = [-1,-2]
#
# def min_pos(a):
#     b = []
#     for i in range(len(a)+1):
#         b.append(i)
#     for j in a:
#         if j > 0:
#             result = list(set(a) ^ set(b))
#         else:
#             result = [1]
#     return result[0]
#
# print(min_pos(a))

#2
# print(max_binary_gap(n))
# def solution(n):
#     res = 0
#     st = -1
#     for i in range(n.bit_length()):
#         if n & (1 << i):
#             if st != -1:
#                 res = max(res, i - st - 1)
#             st = i
#
#     return res
#
# print(solution(n))

# 3
# a = [1,2,3,4]
#
# def shifted(a, n):
#     return a[-n:] + a[:-n]
#
# print(shifted(a, 4))

