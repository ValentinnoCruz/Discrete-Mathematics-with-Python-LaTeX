

# predefined functions

# --------------------------------------- example 1 ---------------------------------------

it = [2,4,6,22,45,7]


 # ma = max (it) # gives us max function from it value. CALLED CALLING THR FUNCTION

 # print(ma)   # this makes it actually print.




# --------------------------------------- example 2 ---------------------------------------

print(len(it)) # this will print 6?


# print("length of the list:" + len(it)) # this will not work cuz string and int

print("length of the 1st list:" + str(len(it)))


# --------------------------------------- example 3 overloading ---------------------------------------

it_2 = ["john","cat", 4,2.3]
print("length of the 2nd list:" + str(len(it_2))) # even though it has 2 diff types of elements it
                                                  # will still tell us how many are in the lsit.


# --------------------------------------- example 4 overloading more than one arguemnt  ---------------------------------------
# all ints
min_1 = min(1,2,5,11,66)
print(min_1) # prints out the lowest number in the above list


# --------------------------------------- example 4 overloading more than one arguemnt 2 ---------------------------------------

min_2 = min(it)
print(min_2)  # prints out the lowest number in the above list

# --------------------------------------- example 5 ---------------------------------------

# this will print out in lexical order (similar to alphabetical) this will give us the result 2 which is the place for CAT alpha first
it_str = ["Mouse", "cat", "racoon"] # this is overloading
min_3 = min(it_str)


# --------------------------------------- example 5  define a new function---------------------------------------
# user defined function

def f(x,y):
    return 2*x+y**2 #must be indented


f(4,8)
print(f(4,8))

x= 4
y=8



# --------------------------------------- example 6  define a new function---------------------------------------
# user defined function

def f(x,y):
    x = x+7
    return
    2 * x + y ** 2


f(4,8)
print(f(4,8))

# --------------------------------------- example 7  define a new function---------------------------------------

# body of function

def equal (x,y):
    if x==y:
        return("if they are equal")

result = equal(3,3)
print("printing...", result )


# --------------------------------------- example 7  define a new function---------------------------------------

#using multiple return in a function

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print("The number is even",even(23))


# --------------------------------------- example 9not returning a value ---------------------------------------


x = 5
y= 10
z=15


def double (m):
    x = m*m
    print(x)

double(x)
print(x)
double(y)
print(y)
double(z)
print(z)

# --------------------------------------- example 10 not returning a value ---------------------------------------


x = 5
y= 10
z=15


def double (m):
    x = m*m
    print(x)
    return(x)


print(x)
var = double (x)
print(var+5)
double(y)
print(y)
double(z)
print(z)


# --------------------------------------- example 11  ---------------------------------------

#

set_1 = {1,2,3,4,6,2,3}

def con(s, x):
    for y in s:
            if y==x:    # wont print the second set cuz its not in it.
                print("The value is in the set")
                break;

con(set_1, 4) #in the set
con(set_1,7) # not in the set


# --------------------------------------- example 12  ---------------------------------------


con(set_1,4)
con(set_1, 44)

set_2 = {1,2,4, "cats", 3.3}

print(set_2) # will put it in numberical first than put cats at the back of it
print(set_1)
