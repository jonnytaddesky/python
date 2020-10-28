p1 = "   Bang!     "
p2 = "     Bang!   "

def whos_first(p1, p2):
    if p1.find('B') < p2.find('B'):
        return 'p1'
    elif p1.find('B') > p2.find('B'):
        return 'p2'
    elif p1.find('B') == p2.find('B'):
        return 'tie'