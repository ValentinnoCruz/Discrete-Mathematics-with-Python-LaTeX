# You are not allowed to import any modules whatsoever

# Assume a set is represented as a Python list

# Do not modify these
A = [1, 2, 5, 8, 12, 5]
B = [3, 5, 7, 8, 11, 3]


# ====================        ====================
# ====================        ====================
# ==================== Part 1 ====================
# ====================        ====================
# ====================        ====================

# Define a function that takes in a set, represented as a Python list,
# and returns an equivalent set with all duplicates removed
def simplify(A):
    result = []  # this will store the non - duplicate elements
    #run the loop to list
    for i in range(len(A)):
        # check if element is in result
        if A[i] not in result:
            # add element to result if it is not present
            result.append(A[i])  # if it is not present then add that element to result
    # return
    return result


# Testing the simplify function
print("A = ", simplify(A))
print("B = ", simplify(B))

# Expected:
# A =  [1, 2, 5, 8, 12]
# B =  [3, 5, 7, 8, 11]

print


# ====================        ====================
# ====================        ====================
# ==================== Part 2 ====================
# ====================        ====================
# ====================        ====================

# Define a function that takes in two sets and returns their union.
# The resulting set should be a Python list with no duplicates
def union(A, B):
    result = []
    # Looping through val for A
    for x in A:
        # Check result to make sure there is no x
        if x not in result:
            # Append z to result
            result.append(x)
    # Looping for each val of A
    for x in B:
        # check result to make sure there is no x
        if x not in result:
            # Append x to result
            result.append(x)
    # Returning result
    return result


# Testing the union function
print("A union B = ", union(A, B))

# Expected:
# A union B =  [1, 2, 5, 8, 12, 3, 7, 11]

print



# ====================        ====================
# ====================        ====================
# ==================== Part 3 ====================
# ====================        ====================
# ====================        ====================


# Define a function that takes in two sets and returns their intersection.
# The resulting set should be a Python list with no duplicates
def intersection(A, B):
    result = []
    # Looping for each val of A
    for x in A:
        # Checking B to find x
        if (x in B) and (x not in result):
            # Appen X to result
            result.append(x)
    # Return
    return result


# Testing the intersection function
print("A intersection B = ", intersection(A, B))

# Expected:
# A intersection B =  [5, 8]

print



# ====================        ====================
# ====================        ====================
# ==================== Part 4 ====================
# ====================        ====================
# ====================        ====================


# Define a function that takes in two sets, A and B, and returns True
# if A is a subset of B, and False otherwise
def subset(A, B):
    for val in A:
        if val not in B:
            return False
    return True



# Testing the subset function


print("A subset of B:", subset(A, B))
print("[5, 7, 8] subset of B:", subset([5, 7, 8], B))

# Expected:
# A subset of B: False
# [5, 7, 8] subset of B: True

print


# ====================        ====================
# ====================        ====================
# ==================== Part 5 ====================
# ====================        ====================
# ====================        ====================

# Define a function that takes in two sets and returns True
# if they are equal, and False otherwise
def equal(A, B):
    return subset(A, B) and subset(B, A)

# Testing the equal function
print("A == B:", equal(A, B))
print("[1, 2, 3, 4] == [1, 1, 2, 2, 4, 2, 3, 3]:", equal([1, 2, 3, 4], [1, 1, 2, 2, 4, 2, 3, 3]))

# Expected:
# A == B: False
# [1, 2, 3, 4] == [1, 1, 2, 2, 4, 2, 3, 3]: True

print


# ====================        ====================
# ====================        ====================
# ==================== Part 6 ====================
# ====================        ====================
# ====================        ====================

# Define a function that takes in two sets and returns their Cartesian product
# The result should be represented as a list of tuples, ex: [(1, 1), (1, 2), ...]
def cartesian_product(A,B):
    pro=[]
    for i in A:
        for j in B:
            if (i,j) not in pro:
                pro.append((i,j))
    return pro
cartesian_product([1,2,3],[4,5,6])

# Provide your code here...


# Testing the cartesian_product function
print("[1] x B =", cartesian_product([1], B))
print("[1, 2] x B =", cartesian_product([1, 2], B))
print("[] x B =", cartesian_product([], B))

# Expected:
# [1] x B =  [(1, 3), (1, 5), (1, 7), (1, 8), (1, 11)]
# [1, 2] x B =  [(1, 3), (1, 5), (1, 7), (1, 8), (1, 11), (2, 3), (2, 5), (2, 7), (2, 8), (2, 11)]
# [] x B =  []

print


# ====================        ====================
# ====================        ====================
# ==================== Part 7 ====================
# ====================        ====================
# ====================        ====================

# Define a function that takes in a set and returns its power set
# The result should be represented as a list of lists, ex: [[], [1], [2], [1, 2]]
def power_set(a):
    temp=[]
    arr=[]
    ps=[]
    s=""
    for i in range(pow(2,len(a))):
        arr=[]
        s="0"*(len(a)-len(bin(i)[2:]))+bin(i)[2:]
        temp=list(s)
        for j in range(len(temp)):
            if temp[j]=="1":
                arr.append(a[j])
        if arr not in ps:
            ps.append(arr)
    return ps
power_set([1,2,3,4])

# Provide your code here...


# Testing the power_set function
print("P([1, 2, 3]) =", power_set([1, 2, 3]))
print("P([]) =", power_set([]))

# Expected:
# P([1, 2, 3]) =  [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# P([]) = [[]]
