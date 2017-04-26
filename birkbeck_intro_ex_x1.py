# What does this program do? This question is not about describing the instructions in
# the program one by one. Instead, try to find a descriptive name as a "summary" to tell
# the user of the program what output it will compute based on the user's inputs. Try to
# answer this question without using a computer.

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