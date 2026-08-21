""" Question 2: shortest_string_length """
"""
Input: list of strings
Output: length of shortest string in list
"""
def shortest_string_length(L):
    count=0
    for c in L:
        length=len(c)
        if length<count or count==0:
            count=length
    return count

""" Test 2 """
def test_shortest_string_length():
    print("Testing shortest_string_length...", end='')
    L0 = ["hi", "hello", "howdy"]
    assert(shortest_string_length(L0) == 2)
    L1 = ["goodbye", "pineapple", "hello"]
    assert(shortest_string_length(L1) == 5)
    L2 = ["a", "b", "c"]
    assert(shortest_string_length(L2) == 1)
    print("... done!")


if __name__ == '__main__':
    test_shortest_string_length()