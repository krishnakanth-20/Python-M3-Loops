""" Question 1: n_fours """
"""
Input: integer n
Output: integer with n 4s
"""
def n_fours(n):
    if n==0:
        return n
    total=0
    for i in range(n):
        total=total+(10**i)*4
    return total

""" Test 1 """
def test_n_fours():
    print("Testing n_fours...", end='')
    assert(n_fours(0) == 0)
    assert(n_fours(1) == 4)
    assert(n_fours(2) == 44)
    assert(n_fours(3) == 444)
    assert(n_fours(5) == 44444)
    assert(n_fours(8) == 44444444)
    print("... done!")

if __name__ == '__main__':
    test_n_fours()
