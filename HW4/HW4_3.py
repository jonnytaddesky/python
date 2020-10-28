def calc_dice_scores(lst):
    # for x in lst:
    #     if x[0] == x[1]:
    #         print(0)
    #         break
    #     elif x[0] != x[1]:
    #         print(sum([x[0]+x[1] for x in lst]))
    #         break
    print(sum([a+b for a, b in lst]) if not any([a==b for a, b in lst]) else 0)

calc_dice_scores([(2, 1), (4, 5), (4, 5)])

# string = [(2, 1), (4, 5), (4, 5)]

# for x in string:
#     if x[0] == x[1]:
#         print(0)
#         break
#     else:
#         print(sum([x[0]+x[1] for x in string]))
#         break
