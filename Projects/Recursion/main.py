
import random
import time


# Generate random numbers list
def generate_ranlist(n):
    s = []
    for i in range(n):
        # generate a ran int b/w 1 to n
        s.append(random.randint(1, n))

    return s


# search linearly
def linear_search(s, k):
    for i in range(len(s)):
        if s[i] == k:
            return i  
    # when not found return -1
    return -1

# search num using bin search
def binary_search(s, k):
    left = 0
    right = len(s) - 1
    while left <= right:


        middle = (left + right) // 2
        # same middle
        if s[middle] == k:
            return middle
        # search left space
        elif s[middle] > k:
            right = middle - 1
        # search right space
        else:
            left = middle + 1
    # when not found
    return -1


## main function

# 10^2 - 10^9

print('{:<10}{:<25}{}'.format('Size', 'Linear Search', 'Binary Search'))
for size in range(2, 10):
    # gen the ran num list
    s = generate_ranlist(10 ** size)

    # calculate time
    l_start_time = time.perf_counter()
    linear_search(s, -1)
    l_spent_time = time.perf_counter() - l_start_time

    # sort the list f
    s.sort()
    # calculate time (worst case)
    binary_time = time.perf_counter()
    binary_search(s, -1)
    b_spent_time = time.perf_counter() - binary_time
    # tabulate result
    print('{:<10}{:<25}{}'.format(10 ** size, l_spent_time, b_spent_time))