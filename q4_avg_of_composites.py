""" Question 5: average_of_composites """
"""
Input: list of integers
Output: average of composite numbers in list
"""
def is_prime(num):
    if (num<=1):
        return False
    for possible_factor in range(2, num):
        if (num % possible_factor == 0):
            return False
    return True

def average_of_composites(L):
    if L=="":
        return 0
    total=0
    count=0
    for i in list(L):
        if not(is_prime(i)):
            total+=i
            count+=1
    if total==0:
        return 0
    else:
        return total/count

""" Test 6 """
import math
def test_average_of_composites():
    print("Testing average_of_composites...", end='')
    assert(average_of_composites([]) == 0)
    assert(average_of_composites([4]) == 4)
    assert(average_of_composites([4, 6, 8]) == 6)
    assert(average_of_composites([2, 5, 7]) == 0)
    assert(average_of_composites([4, 6, 8, 9, 10]) == 7.4)
    print("... done!")


if __name__ == '__main__':
    test_average_of_composites()