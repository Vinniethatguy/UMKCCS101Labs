########################################################################
##
## CS 101 Lab
## Program # 10
## Name Vince Smith
## Email vasy9z@umsystem.edu
##
## PROBLEM : Describe the problem
## 
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
## For some reason my play agian function is not working. Do I need to add a break statment?
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################



import csv
def maxFinder(file):
    largest = (-1, -1)
    for key in file.keys():
        if file[key] > largest[1]:
            largest = (key, file[key])
    return largest


def month_from_number(number):
    months = {1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

    try:
        if int(number) < 1 or int(number) > 12:
            print("invalid number")
        else:
            return months[int(number)]
    except:
        print("invalid number")

def create_reported_date_dict(file):
    prod = {}
    for val in file:
        if val[1] in prod.keys():
            prod[val[1]] += 1
        else:
            prod[val[1]] = 1
    return prod

def create_reported_month_dict(file):
    prod = {}

    for val in file:
        temp = int(val[1][:2])
        if temp in prod.keys():
            prod[temp] += 1
        else:
            prod[temp] = 1
    return prod

def create_offense_dict(file):
    prod = {}
    for val in file:
        if val[7] in prod.keys():
            prod[val[7]] += 1
        else:
            prod[val[7]] = 1

    return prod

def create_offense_by_zip(file):
    # 7 crime
    # 13 zip code
    prod = {}
    for val in file:
        if val[7] in prod.keys():
            try:
                prod[val[7]][val[13]] += 1
            except:
                prod[val[7]][val[13]] = 1
        else:
            prod[val[7]] = {val[13]:1}
    return prod

if __name__ == '__main__':
    while True:
        try:
            filename = input("Enter the name of the crime data file ==> ")
            file = open(filename, encoding='utf-8')
            break
        except:
            if filename =='':
                print("Could not find the file specified. not exists not found")
            else:
                print("Could not find file specified.",filename,'not found')
    file_csv = csv.reader(file)
    fullFile = []
    for line in file_csv:
        fullFile.append(line)


    month = create_reported_month_dict(fullFile[1:])
    mlargest = maxFinder(month)
    crime = create_offense_dict(fullFile[1:])
    clargest = maxFinder(crime)

    print("The month with the highest of crimes is",month_from_number(mlargest[0]), 'with', mlargest[1],'offences')
    print('The offense with the highest # of crimes is',clargest[0], 'with',clargest[1])

    zipCrimes = create_offense_by_zip(fullFile[1:])
    while True:
        offense = input('Enter an offense: ')
        if offense in zipCrimes.keys():
            break
        else:
            print("Not a valid offense found, please try again")

    print(offense, 'offenses by Zip Code')
    print('{:<10}{:>20}'.format('Zip Code', '# Offenses'))
    print('=' * 30)
    for key in zipCrimes[offense].keys():
        print('{:<10}{:>20}'.format(key,zipCrimes[offense][key]))