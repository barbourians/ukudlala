from __future__ import print_function

# 1. A Python instruction which would output a blank line.
if False:
    print ('A Python instruction which would output a blank line.')
    print ('')
    
# 2. An instruction which would output: Hickory, Dickory, Dock
if False:
    print ('An instruction which would output: Hickory, Dickory, Dock')
    print ('Hickory')
    print ('Dickory')
    print ('Dock')

# 3. A program which reads in two words, one after the other, and then displays them in reverse order.
#    For example, if the input was
#        First
#        Second
#    The output should be
#        Second
#        First
if True:
    print ('A program which reads in two words, one after the other, and then displays them in reverse order.')
    print ('First word: ', end='')
    word1 = raw_input()
    print ('Second word: ', end='')
    word2 = raw_input()
    print (word2)
    print (word1)