
#----------------------------------------------
#absolute_sort()
#----------------------------------------------

#A tuple as input, with numbers.
#Sort it by absolute value in ascending order. 

#For example, the tuple (-20, -5, 10, 15) will be sorted to: (-5, 10, 15, -20). 
#Your function should return the sorted list or tuple.

#Example:

#	absolute_sort((-20, -5, 10, 15)) == [-5, 10, 15, -20]
#		or
#	absolute_sort((-20, -5, 10, 15)) == (-5, 10, 15, -20)

#	absolute_sort((1,2,3,0)) == [0,1,2,3]
#		or 
#	absolute_sort((1,2,3,0)) == (0,1,2,3)

#Precondition:
#- Input tuple contains only unique integers.
#- If x in input tuple, -x is not in input.

#Your task:

#1. Replace body of absolute_sort() with something that works.

#def absolute_sort(t):
 #   return []

#2. Write some test code to prove your solution works.



#import module for unit testing:
import unittest

# function to sort a tuple by absolute value and return a list:
def absolute_sort(t):
    print t,
    print " : ",
    # convert the tuple to a list so we can mess with it
    t_list = list(t)
    # use the key argument of the sort() and sorted() functions
    # in this case the abs() function
    print sorted(t_list,key=abs)
    return sorted(t_list,key=abs)

# define test cases:    
class TestAbsSort(unittest.TestCase):

    def test_01(self):
        self.assertEqual(absolute_sort((-5,4,2,7)),[2,4,-5,7])

    def test_02(self):
        self.assertEqual(absolute_sort((1,8,500,-2)),[1,-2,8,500])

    def test_03(self):
        self.assertEqual(absolute_sort((-20, -5, 10, 15)),[-5,10,15,-20])

    def test_04(self):
        self.assertEqual(absolute_sort((1,2,3,0)),[0,1,2,3])
        


# this if block means if we call this file (name.py) directly,
# then run the unit tests on our code:
if __name__ == '__main__':
#   unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAbsSort)
    unittest.TextTestRunner(verbosity=2).run(suite)
