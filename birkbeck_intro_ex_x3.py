
# Write a program that takes a series of numbers (ending in 0) and counts the number of
# times that the number 100 appears in the list.
# For example, for the series 2, 6, 100, 50, 101, 100, 88, 0, it would output 2.

from __future__ import print_function

m = 0
finished = False
while not finished:
    print('Enter another number (0 to finish): ', end='')
    s = raw_input()
    num = int(s)
    if num != 0:
        if num == 100:
            m = m + 1
    else:
        finished = True

print('The number 100 appears',str(m),'times.')