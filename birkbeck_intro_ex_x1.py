# Exercise X1
m = 0
finished = False
while not finished:
    print('Enter another number (0 to finish): ')
    s = input()
    num = int(s)
    if num != 0:
        if num > m:
            m = num
    else:
        finished = True

print(str(m))