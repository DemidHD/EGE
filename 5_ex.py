for i in range(1, 1000):
    bin_x = bin(i)[2:]
    if i % 2 == 0:
        bin_x = bin_x + '01'
    else:
        bin_x = '1' + bin_x + '10'

    if int(bin_x, 2) > 214:
        print(i)
        break
