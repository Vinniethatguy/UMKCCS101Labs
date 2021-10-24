########################################################################
##
## CS 101 Lab
## Program #8
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

illegalChars = ['#', '%', '&', '{', '}', '\\', '+', '`', '|'
                '=', '<', '>', '*','?', '/',' ','$', '!', "'",
                '"', ':', '@']
minimum = 0.0
while True:
    try:
        #------- temp variable location CHANGE ME!! ---------
        minimum = float(input('Enter the minimum mpg: '))
        #minimum = 20

        if minimum > 0 and minimum < 100:
            break
        elif minimum < 0:
            print('Fuel economy given must be greater than 0')
        elif minimum > 99:
            print('Fuel economy must be less than 100')
    except:
        print("You must enter a number for the fuel economy")

invalidCar = []
finalValues = []

while True:
    # fileName = input('Enter the name of the input vehicle file: ')
    fileName = './lab08.py/' + "vehicles.txt"
    try:
        with open(fileName, 'r') as file:
            for line in list(file)[1:]:
                parts = line.split('\t')
                check = parts[-3]
                try:
                    if float(check) >= minimum:
                        finalValues.append([parts[0], parts[1], parts[2], parts[-3]])
                except:
                    invalidCar.append(parts[0] + ' ' + parts[1] + ' '+parts[2])

            break
    except:
        print('Could not open file', fileName)

example = 1
# print("{0:.3f}".format(example))
print(invalidCar)
finalValues = [[val if num != 3 else str("{0:.3f}".format(float(val))) for num, val in enumerate(x)] for x in finalValues]
t = ' '
with open('output.txt', 'w') as file:
    for values in finalValues:
        print('{:1} {:10}          {:<40}{}'.format(values[0],values[1],values[2],values[3]), file=file)