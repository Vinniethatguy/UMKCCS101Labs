########################################################################
##
## CS 101 Lab
## Program #7
## Name Vince Smith
## Email vasy9z@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
#
#
#
#
##
########################################################################


def Cypher(word, key):
    word = word.upper()
    cWord = " "
    for letter in word:
        if letter.isalpha():
            cWord += chr(ord('A') + ((ord(letter) - 65 + key) % 26))
        else:
            cWord += letter
    return cWord

def DeCypher(cWord, key):
    cWord = cWord.upper()
    word = " "
    for letter in cWord:
        if letter.isalpha():
            word += chr(ord('A') + ((ord(letter) - 65 - key) % 26))
        else:
            word += letter
    return word


print("Main Menu")
print("1) Encode a string")
print("2) Decode a string")
print("Q) Quit")
Selection = str(input("Enter your Selection "))

if Selection == "1":
    word = input("Enter (brief) text to encrypt:")
    key = 3
    cval = Cypher(word, key)
    print(cval)    
if Selection =="2":
    word = input("Enter (brief) text to encrypt:")
    key = 3
    val = DeCypher(word, key)
    print(val)
if Selection == "Q":
    quit

