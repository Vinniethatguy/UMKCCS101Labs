########################################################################
##
## CS 101 Lab
## Program #9
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



import math

def meanFinder(items):
    if not items:
        return 'n/a'

    # "{:.2f}".format()
    return sum(items)/len(items)

def stdFinder(items):
    if not items:
        return 'n/a'
    top = sum([(x - meanFinder(items)) ** 2 for x in items])
    return math.sqrt(top/len(items))

def displayScore(Tests, Assignments):
    topLine = "{:<10} {: >16} {: >16} {: >16} {: >16} {: >16}".format('Type','#','min','max','avg','std')
    print(topLine)
    print('=' * len(topLine))
    try:
        tMean = "{:.2f}".format(meanFinder(Tests))
        aMean = "{:.2f}".format(stdFinder(Assignments))
        tStan = "{:.2f}".format(stdFinder(Tests))
        aStan = "{:.2f}".format(stdFinder(Assignments))
    except:
        tMean = "n/a"
        aMean = "n/a"
        tStan = "n/a"
        aStan = "n/a"
    print("{:<10} {: >16} {: >16} {: >16} {: >16} {: >16}".format('Tests',len(Tests),min(Tests, default='n/a'),max(Tests, default='n/a'), tMean, tStan))
    print("{:<10} {: >16} {: >16} {: >16} {: >16} {: >16}".format('Programs',len(Assignments),min(Assignments, default='n/a'), max(Assignments, default='n/a'),aMean, aStan))

    if not Tests or not Assignments:
        print('The weighted scores is','                   ','0.00')
    else:
        print('The weighted scores is ','                   ',(meanFinder(Tests) * .6) + (meanFinder(Assignments) * .4))



def adder(items, type):
    choice = input('Enter the new ' + type + ' score 0-100 ==>')
    try:
        choice = float(choice)
        if choice < 0:
            print("Invalid value\n")
        else:
            items.append(choice)

    except:
        print("Invalid value\n")

def remover(items, type):
    print(items)
    choice = input('Enter the ' +type +' to remove 0-100 ==> ')
    try:
        items.remove(float(choice))
    except:
        print("Invalid value\n")

def displayMenu():
    print('1 -Add Test')
    print('2 -Remove Test')
    print('3 -Clear Tests')
    print('4 -Add Assignment')
    print('5 -Remove Assignment')
    print('6 -Clear Assignments')
    print('D -Display Scores')
    print('Q -Quit',end='\n\n')
    return input('==> ')

def decision(choice, Tests, Assignments):
    choiceList = ['1', '2', '3', '4', '5', '6', 'd', 'D', 'q', 'Q']
    while choice not in choiceList:
        print("Invalid selection")
        choice = displayMenu()
    if choice == '1':
        adder(Tests, 'Test')
    elif choice == '2':
        remover(Tests, 'Test')
    elif choice == '3':
        Tests.clear()
    elif choice == '4':
        adder(Assignments, 'Assignment')
    elif choice == '5':
        remover(Assignments, 'Assignment')
    elif choice == '6':
        Assignments.clear()
    elif choice == 'd' or choice == 'D':
        displayScore(Tests, Assignments)
    elif choice == 'q' or choice == 'Q':
        quit()





Tests = []
Assignments = []

while True:
    choice = displayMenu()
    decision(choice, Tests, Assignments)

