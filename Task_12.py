a = input('Print something here: ')
a = a.lower()
if a.count('f'):
    b = a.index('f')
    c = a.rindex('f')
    print("Number of characters found: " + str(a.count('f')))
    print("First index: " + str(b))
    print("Last index: " + str(c))
else:
    print("Symbol 'f' not found")
