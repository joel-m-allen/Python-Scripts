print("Hello World!")

# script to play with data types: examine the implicit type changes with some math ops, and the direct
#   typing functioons int() and float()
# created on python 2.7.12 on windows, with IDLE.
       
a = raw_input('Enter a Number: ')
b = raw_input('Now Enter another Number: ')

sum = a+b
print('Data type sum:', sum, type(sum))
sum = int(a)+ int(b)
print('Data type sum:', sum, type(sum))
sum = float(sum)
print('Data type sum:', sum, type(sum))
#sum = char(int(sum))
#print('Data type sum:', sum, type(sum))
