
#import module for unit testing:
import unittest

# function print responses based on number input:
def fizzbuzz(num):
    response = ""
    if not (0<num <=1000):
        response = "input out of range"
        return response
    
    # to check for divisibility, we use the modulo % function.
    # modulo x % y returns the remainder when x is divided by y
    # when y goes evently into x, x%y =0
    if (not num % 3):
        response = response+"Fizz "
    if (not num % 5):
        response = response+"Buzz"
    if ((num % 3) and (num % 5)):
        response = str(num)
    # remove the trailing whitespace if we have the "Fizz"-only case:
    response = response.strip()
    return response

# define test cases:    
class TestFizzBuzz(unittest.TestCase):

    def test_01(self):
        print "3:",
        print fizzbuzz(3),
        print " ",
        self.assertEqual(fizzbuzz(3),"Fizz")

    def test_02(self):
        print "15:",
        print fizzbuzz(15),
        print " ",
        self.assertEqual(fizzbuzz(15),"Fizz Buzz")

    def test_03(self):
        print "2:",
        print fizzbuzz(2),
        print " ",
        self.assertEqual(fizzbuzz(2),"2")

    def test_04(self):
        print "1001:",
        print fizzbuzz(1001),
        print " ",        
        self.assertEqual(fizzbuzz(1001),"input out of range")
        


# this if block means if we call this file (name.py) directly,
# then run the unit tests on our code:
if __name__ == '__main__':
#   unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFizzBuzz)
    unittest.TextTestRunner(verbosity=2).run(suite)
