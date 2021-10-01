########################################################################
##
## CS 101 Lab
## Program #
## Name Vince Smith
## Email vasy9z@umsystem.edu
##
## PROBLEM : Describe the problem
## The problem is, we're making a slot machince game like the one you see at the casino. The machine is one pull with 3 reels
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

#import modules needed

import random

def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    ask = input("Do you want to play again?")
    if ask=='N' or ask=='NO':
            return False
    elif ask=='Y' or ask=='YES':
            return True
    else:
            return play_again()

def get_wager(amount):
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    ask=int(input("How many chips would you like to wager?"))
    
    if 0 < ask and amount >= ask:
        return ask
    else:
        return get_wager(amount)
        
def get_slot_results():
    ''' Returns the result of the slot pull '''

    return random.randint(1,10)
    
def get_matches(reela, reelb, reelc):
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

    if reela == reelb and reelb==reelc:
        return 3
    elif reela == reelb or reelb == reelc or reelc == reela:
        return 2
    else:
        return 0
        
def get_bank():
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''

    ask=int(input("How many chips do you want to play with?"))
    
    if ask>0 and ask<101:
        return ask
    else:
        return get_bank()
        
def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''

    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 5
    else:
        return wager *- 1
        
if __name__=="__main__":
    
    playing =True
    
    while playing:
        
        bank = get_bank()
        
        while bank >0:
            
            wager = get_wager(bank)
            reel1 = get_slot_results()
            reel2 = get_slot_results()
            reel3 = get_slot_results()
            
            matches = get_matches(reel1,reel2,reel3)
            
            payout = get_payout(wager,matches)
            bank = bank + payout
            
            print("Your spin",reel1,reel2,reel3)
            print("You matched",matches, "reels")
            print("You won/lost",payout)
            print("Current bank", bank)
            print()
        
        print("You lost all",0,"in",0,"spins")
        print("The most chipe you had was",0)
        playing=play_again()