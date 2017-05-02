# Write a solution for exercise X5 that prints all the 'Down', 'Same', and 'Up' messages together at the end.
#
# Enter the first number: 3
# Enter the next number (0 to finish): 5
# Enter the next number (0 to finish): 4
# Enter the next number (0 to finish): 4
# Enter the next number (0 to finish): 6
# Enter the next number (0 to finish): 8
# Enter the next number (0 to finish): 2
# Enter the next number (0 to finish): 6
# Enter the next number (0 to finish): 7
# Enter the next number (0 to finish): 5
# Enter the next number (0 to finish): 6
# Enter the next number (0 to finish): 6
# Enter the next number (0 to finish): 7
# Enter the next number (0 to finish): 0
#     Up Down Same Up Up Down Up Up Down Up Same Up

# Write a program that takes a series of numbers (ending in 0).
# If the current number is the same as the previous number, it says 'Same';
# If the current number is greater than the previous one, it says 'Up'
# If it's less than the previous one, it says 'Down'.
# It makes no response at all to the very first number.
# For example, its output for the list 9, 9, 8, 5, 10, 10, 0, would be:
#   Same, Down, Down, Up, Same (comparing, in turn, 9 and 9, 9 and 8, 8 and 5, 5 and 10, 10 and 10).
# You may assume there are at least two numbers in the input.
#
# Enter the first number: 9
# Enter the next number (0 to finish): 9
# Same
# Enter the next number (0 to finish): 8
# Down
# Enter the next number (0 to finish): 5
# Down
# Enter the next number (0 to finish): 10
# Up
# Enter the next number (0 to finish): 10
# Same
# Enter the next number (0 to finish): 0

from __future__ import print_function

n1 = 0
n2 = 0
mess = ""
print("Enter the first number: ", end='')
s = raw_input()
n2 = int(s)
finished = False
while not finished:
    n1 = n2
    print("Enter the next number (0 to finish): ", end='')
    s = raw_input()
    n2 = int(s)
    if n2 == 0:
        finished = True
    elif n1 > n2:
        mess = mess + "Down "
    elif n1 < n2:
        mess = mess + "Up "
    else:
        mess = mess + "Same "

print (mess)