from __future__ import print_function

# Now see if you can write a program in Python that takes two words from the keyboard
# and outputs one after the other on the same line. E.g., if you keyed in 'Humpty' and
# 'Dumpty' it would reply with 'Humpty Dumpty' (note the space in between).
# A run of the program should look like this:
#    Please key in a word: Humpty
#    And now key in another: Dumpty
#    You have typed: Humpty Dumpty

print ("Please key in a word: ", end='')
word1 = raw_input()
print ("And now key in another: ", end='')
word2 = raw_input()
print ("You have typed:", word1, word2)