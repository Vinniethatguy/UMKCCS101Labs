
########################################################################
##
## CS 101 Lab
## Program # 15
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
##
########################################################################




import unittest
import Grades

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result,33,"The toal function should return 33")
    
    def test_total_returns_0(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result,0,"The toal function should return 33")
    

unittest.main()