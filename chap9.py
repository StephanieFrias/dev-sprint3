# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Stephanie Frias

#9.1
'''the below code prints words in the txt file that have more than 20 characters.'''
fin = open('words.txt')
for line in fin:
	word = line.strip()
	if len(word) > 20:
		print word

#9.2
'''The below code prints True if a word does not have an 'e' and False if a word does have an 'e'.'''
def has_no_e(word):
	if word.find('e') == -1:
		print True
	else:
		print False
		
has_no_e('wishful')
has_no_e('elephant')

'''The below code prints all words in the txt file without an 'e' in them.'''

fin = open('words.txt')
for line in fin:
	word = line.strip()
	if word.find('e') == -1:
		print word

'''The below code counts words in the txt file with an e, then counts words in the txt file without an e.
It then adds these two figures and supplies the percentage of words in the txt file without an e.'''

fin = open('words.txt')
wordcount = 0
wordcount2 = 0
for line in fin:
	word = line.strip()
	if word.find('e') != -1:
		wordcount += 1
	elif word.find('e') == -1:
		wordcount2 += 1
	total= float(wordcount+wordcount2)
	percent = float(wordcount2/total)
print wordcount
print wordcount2
print total
print percent

#9.3
'''The below code takes the letters in string, and if these letters are in word, it returns false, 
otherwise, returns true.'''
def avoids(word,string):
	for letter in string:
		if letter in word:
			return False
	return True

print avoids ('blue', 'le')
print avoids ('blue', 'ac')
print avoids ('blue', 'la')	
	
'''The below code asks the user to input forbidden characters. For each forbidden characters found 
in each word, count 1 increases by 1. For each forbidden character not found in the word, 
count2 increase by 1. It then divides count2 by the length of the forbidden string, to reveal the number
of words that do no contain any of the forbidden characters.'''

fin = open('words.txt')
line = fin.readline()
count = 0
count2 = 0
forbidden = raw_input('Type in a string of forbidden characters.\n')
for line in fin:
	word = line.strip()
	for letter in forbidden:
		if letter in word:
			count += 1
		if letter not in word:
			count2 += 1	
			divide= count2/len(forbidden)
print divide

#9.4
'''The below code returns False for any letter in word that is not a letter in string. 
Otherwise, it returns True.'''
def uses_only(word, string):
	for letter in word:
		if letter not in string:
			return False
	return True

print uses_only('blue','eulb')