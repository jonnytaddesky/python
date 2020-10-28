def any_duplicates(square):
    #  for x in square:
    #      print(x)
    # if sum([x+y+z for x,y,z in square]) == 45:
    #     print(False)
    # else:
    #     print(True)

    print(True if sum([x+y+z for x,y,z in square]) != 45 else False)

any_duplicates([[8, 9, 2], [6, 5, 1], [3, 7, 4]])