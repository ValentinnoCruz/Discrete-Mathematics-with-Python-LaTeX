print("Helo world!")
x = 5
print(x)
# this is how we do a coment

"""
this can be a multi- use coment
"""
#example 2
x = 5
# the name x asociates to the data (5)
# lok how we did not assoicate x as a variable (var x; //js) (var x=6;)


x = 5
print(x)
#x=float(5)

x=float(5)
print(x)
# using it as a float wil give us a decimal number

#example 3
y = "$"
print(y)
# will print as a char

#example 4
print(type(y))

#example 5
a,b,c = 1, 2, 3
print(a)
print(b)
print(c)

# ex 6
d = e = f = 12
print(d)
print(e)
print(f)

# example 7
if d == 10:
    print("Even!")
elif d ==11:
    print("odd")
else:
    print("bingo!")
        #since d is not 10 or 11 it will print bingo (both not true)

"""
# example 7.5       # this will give you error because the system will be waiting
if d == 10:         # for a block in else, but treats prints as single codes
    print("Even!")
elif d ==11:
    print("odd")
else:
print("bingo!")
print("yahoo!")
"""

#-----------------------
#-----------------------

"""
# example 8     # this will print 1 infinitely 

z = 1

while z < 5:
    print(z)
"""

#-----------------------
#-----------------------

# example 8.5
z = 1

while z < 5:
    print(z)    # this incremeints the value and count upward
    z += 1       # it will stop at 4

#-----------------------
#-----------------------

# example 8.3

z = 1

while z <= 5:
    print(z)    # this incremeints the value and count upward
    z += 1       # it will stop at 5

#----------------------------------
#----------------------------------

# example 8.4

z = 1

while z <= 5:
    print("the value is:" +str (z))    # this incremeints the value and count upward
    z += 1                             # and will add the string to the front of it


#----------------------------------
#----------------------------------
    
"""

# example 9    #ageOfClien (camel)
               #age_of_client (snake)

age = input("enter your age")

"""

"""

# example 9.2    #this will not work cuz input outputs a char and we
                # are trying ttttto add it to an int

age = input("enter your age")
aged = age + 10

"""

# example 9.3    #ageOfClien (camel)
                 #age_of_client (snake)

age = input("enter your age")

#aged = age + 10
aged = int(age) + 10
print(aged)







