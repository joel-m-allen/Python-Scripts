#print("Hello World!")

# script to play with bitwise operators and in-place data swapping

a = raw_input('Enter a Number: ')
b = raw_input('Now Enter another Number: ')

a = int(a)
b = int(b)

print("a=", a, "\tb= ", b)
# use bitwise xors to swap the variables without using a third var
a = a^b
b = a^b
a = a^b
print("a=", a, "\tb= ", b)

