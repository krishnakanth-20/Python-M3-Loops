""" Question 3: num_even_digits """
"""
Input: integer n
Output: number of even digits in n
"""
def num_even_digits(n):
    if n==0:
        return 1
    count=0
    while n>0:
        digit=n%10
        if digit%2==0:
            count+=1
        n=n//10
    return count

""" Test 3 """
def test_num_even_digits():
    print("Testing num_even_digits...", end='')
    assert(num_even_digits(0) == 1)
    assert(num_even_digits(3) == 0)
    assert(num_even_digits(24) == 2)
    assert(num_even_digits(3376) == 1)
    assert(num_even_digits(3795) == 0)
    assert(num_even_digits(68428) == 5)
    print("... done!")


if __name__ == '__main__':
    test_num_even_digits()