from fnmatch import fnmatch

for i in range(0, 10**8 + 1, 149):
    if fnmatch(str(i), '11*223'):
        print(i, i // 149)


"""второе решение"""
for i in range(0, 10**8 + 1, 149):
    if str(i)[:2] == '11' and str(i)[-3:] == '223':
        print(i, i // 149)