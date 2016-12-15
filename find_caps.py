#----------------------------------------------
#find_caps() -problem statement
#----------------------------------------------

#You are given a chunk of text. 
#Gather all capital letters in one word in the order that they appear in the text.

#Input: A text as a string.

#Output: Capital letters in the string.

#Example:

#	find_caps("George Washington") == "GW"
#	find_caps("John Adams") == "JA"
#	find_caps("wHat AbouT This Example of Reasonable text?") == "HATTER"
#	find_caps("") == ""
    
#Precondition: 
#- Input text will be a string with length between 0 and 1000.
#- All characters in input text are printable.

#Your Task:

#1. Replace body of find_caps() with something that works.

#def find_caps(text):
#    return ""

#2. Write some test code to prove your solution works.
#import module for unit testing:
import unittest

# function to return the caps of a text string
def find_caps(text):
    print text,
    # cycle through text to check each character for upper case 
    caps = [char for char in text if char.isupper()]
    print "".join(caps)
    return "".join(caps)

# define test cases:    
class TestFindCaps(unittest.TestCase):

    def test_GW(self):
        self.assertEqual(find_caps("George Washington"),"GW")

    def test_JA(self):
        self.assertEqual(find_caps("John Adams"),"JA")

    def test_HA(self):
        self.assertEqual(find_caps("wHat AbouT This Example of Reasonable text?"),"HATTER")

    def test_nu(self):
        self.assertEqual(find_caps(""),"")
        

# if we call this file directly, run unit tests:
if __name__ == '__main__':
#   unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindCaps)
    unittest.TextTestRunner(verbosity=2).run(suite)
