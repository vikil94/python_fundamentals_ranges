
for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print('BitMaker')
    elif num % 3 == 0:
        print('Bit')
    elif num % 5 == 0:
        print('Maker')
    else:
        print(num)
