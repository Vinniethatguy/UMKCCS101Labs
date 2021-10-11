########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
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
#ABCDE 1 2 34 5
#FIRST FIVE letters represent student the first 5 letters of students name
#6th value is DIGIT of school and is a value between 1-3
#7th value reprsents grade and shoudld be bewteen 1-4
#The 8th, 9th, and 10thcharacter (index 7, 8, and 9) can only be [0-9]
##
########################################################################






def get_school(school):
    if school == '1':
        return 'School of Computering and Engineering SCE'
    elif school == '2':
        return 'School of Law'
    elif school == '3':
        return 'College of Arts and Sciences'

    return 'Invalid School'


def get_grade(libC):
    if libC[6] == '1':
        return 'Freshman'
    elif libC[6] == '2':
        return 'Sophomore'
    elif libC[6] == '3':
        return 'Junior'
    elif libC[6] == '4':
        return 'Senior'

    return 'Invalid Grade'


def character_value(char):
    letters = {}
    for x in range(0, 26, 1):
        letters[chr(ord('A') + x)] = x
    if char in letters.keys():
        return letters[char]
    return None


def get_check_digit(libC):
    index = 1
    amounts = []
    for x in libC[:-1]:
        if character_value(x) != None:
            amounts.append(character_value(x) * index)
            index += 1
        else:
            amounts.append(int(x) * index)
            index += 1
    return sum(amounts) % 10


def verify_check_digit(libC):
    if len(libC) != 10:
        return (False, "The length of the number given must be 10")
    for num in range(10):
        if num < 5:
            if character_value(libC[num]) == None:
                    return (False, "The first 5 characters must be A-Z, the invalid character is at {} is {}".format(num, libC[num]))
            continue
        for l3 in range(3):
            if not libC[7 + l3].isdigit():
                return (False, "The last 3 characters must be 0-9, the invalid character is at {} is {}".format(7 + l3 ,libC[7 + l3]))
        if num == 5 and not (libC[num] == '1' or libC[num] == '2' or libC[num] == '3'):
            return (False ,"The sixth character must be 1 2 or 3")
        if num == 6 and not (libC[num] == '1' or libC[num] == '2' or libC[num] == '3' or libC[num] == '4'):
            return (False, "The seventh character must be 1 2 3 or 4")
        if num == 9:
            if libC[num] != str(get_check_digit(libC)):
                return False, "Check Digit {} does not match calculated value {}.".format(libC[9], get_check_digit(libC))
    return (True, '')






print(verify_check_digit('V2XYZ58BB'))
print(verify_check_digit('V2XYZ58BBB'))
print(verify_check_digit('VWXYZ58BBB'))
print(verify_check_digit('VWXYZ58593'))
print(verify_check_digit('VWXYZ38593'))
print(verify_check_digit('VWXYZ34593'))
print(verify_check_digit('VWXYZ34592'))
