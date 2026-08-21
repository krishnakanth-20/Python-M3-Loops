""" Question 6: is_consonant """
"""
Input: string s
Output: True if s contains at least one character and every char is a consonant
        False otherwise
"""
def is_consonant(s):
    if s=="":
        return False
    for c in s:
        if (c in "AEIOUaeiou"):
            return False
        if not ("a"<=c<="z" or "A"<=c<="Z"):
            return False
    return True

""" Test 6 """
def test_is_consonant():
    print("Testing is_consonant...", end='')
    # assert(is_consonant("") == False)
    # assert(is_consonant("b") == True)
    # assert(is_consonant("bcdfgh") == True)
    # assert(is_consonant("rtrt") == True)

    # assert(is_consonant("AEIOU") == False)
    # assert(is_consonant("UOIEA") == False)
    # assert(is_consonant("AE") == False)
    # assert(is_consonant("aeiP1") == False)
    # assert(is_consonant("Mnky") == True)
    # assert(is_consonant("Blck") == True)
    # assert(is_consonant("T") == True)
   
    assert(is_consonant("86544") == False)
    assert(is_consonant("234") == False)
    assert(is_consonant("ftftfr12") == False)

if __name__ == '__main__':
    test_is_consonant()