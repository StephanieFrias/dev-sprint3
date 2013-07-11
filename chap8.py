# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Stephanie Frias

#8.12


#My first version of code. Saw it didn't work for all possibilities 
#as I got some interesting characters when using negative integers. Also, I 
#didn't know how to get a string to show up in one line, versus just a character
#per line.
def rotate_word1(string,integer):
	index=0
	while index < len(string):
		newletter=chr((ord(string[index]))+integer)
		result= newletter
		index= index + 1
		print newletter

print rotate_word1('car', -2)

# My second version of code. Saw it didn't work for all possibilities 
#as I got some interesting characters when using negative integers.
def rotate_letter1(letter,number):
	return chr(ord(letter) + number)

print rotate_letter1('c', -5)

#I reviewed the below answer and have a few questions, detailed in my submission.
def rotate_letter2(letter, number):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + number) % 26 + start
    return chr(i)

def rotate_word3(word, number):
    res = ''
    for letter in word:
        res += rotate_letter2(letter, number)
    return res

if __name__ == '__main__':
    print rotate_word3('cheer', 7)
    print rotate_word3('melon', -10)
    print rotate_word3('sleep', 9)