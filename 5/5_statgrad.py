k = 0
for n in range(1000000000, 19876543210):
    bin_x = bin(n)[2:]
    for j in range(2):
        if sum([int(i) for i in str(n)]) % 2 != 0:
            bin_x = bin_x + '1'
        else:
            bin_x = '0' + bin_x
    if 123456789 <= int(bin_x, 2) <= 1987654321:
        k += 1

print(k)
