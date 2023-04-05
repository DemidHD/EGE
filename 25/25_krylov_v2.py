from fnmatch import fnmatch

for i in range(0, 10**8 + 1, 123):
    if fnmatch(str(i), '32*823'):
        print(i, i // 123)


"""второе решение"""
for i in range(0, 10**8 + 1, 123):
    if str(i)[:2] == '32' and str(i)[-3:] == '823':
        print(i, i // 123)