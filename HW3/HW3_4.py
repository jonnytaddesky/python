first_lst = [1, 4, 6, 3, 7, 9, 6, 23, 43]
second_lst = [0, 4, 5, 9, 12, 43, 76, 35, 32]

joined_list = []

# for f in first_lst:
#     if f % 2 != 0:
#         joined_list.append(f)
# for s in second_lst:
#     if s % 2 == 0:
#         joined_list.append(s)
# print(joined_list)


# for f, s in zip(first_lst, second_lst):
#     if f % 2 != 0:
#         joined_list.append(f)
#     if  s % 2 == 0:
#         joined_list.append(s)
# print(joined_list)


odds = [x for x in first_lst if x % 2 != 0]

evens = [x for x in second_lst if x % 2 == 0]

joined_list = odds + evens

print(joined_list)
