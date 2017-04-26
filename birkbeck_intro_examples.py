from __future__ import print_function

if False:
    print('Given a series of words, each on a separate line,')
    print('this program finds the length of the longest word.')
    print('Please enter several words, one per line.')
    print('Finish with a blank line.')
    maxi = 0
    word = '.'
    while len(word) > 0:
        word = raw_input()
        word = word.strip()
        if len(word) > maxi:
            maxi = len(word)

    if maxi == 0:
        print('There were no words.')
    else:
        print('The longest word was '+str(maxi)+' characters long.')
        
if False:
    print('Please key in a word: ', end='')
    word = raw_input()
    print('The word was:', word)


if False:
    word = 'My name is ' + 'Inigo Montoya'
    n = 10 + 7
    text = word + ' and I am ' + str(n)
    print(text)

if False:
    print('Please introduce a number: ', end='')
    word = raw_input()
    n = int(word)
    print('The number was ' + word)
    next = n + 1
    print('The next number is ' + str(next))
    
if False:
    num = 5
    print(str(num))
    num = num + 2
    print(str(num))
    num = num // 3 * 6
    print(str(num))
    print(str(7 + 15 % 4))
    num = 24 // 3 // 4
    print(str(num))
    num = 24 // (num // 4)
    print(str(num))
    
if False:
    s = 'software services'
    s = s[0:4] + s[8:9] + s[13:]
    print(s)
    s = 'artificial reality'
    print(s[11:15] + ' ' + s[0:3])
    length = len(s[11:])
    print(str(length))

if False:
    print('Please key in a number: ', end='')
    s = raw_input()
    num1 = int(s)
    print('And another: ', end='')
    s = input()
    num2 = int(s)
    if num1 == num2:
        print('They are the same.')
        
if True:
    print ('"A" < "9"','A' < '9')
    print ('"Zurich" < "acapulco"', 'Zurich' < 'acapulco')
    print ('"Abba" < "ABBA"','Abba' < 'ABBA')
    print ('"long_thing_with_a_$" < "long_thing_with_a_&"','long_thing_with_a_$' < 'long_thing_with_a_&')
    print ('"King@example.invalid" < "King Kong"','King@example.invalid' < 'King Kong')