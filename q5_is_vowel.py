""" Question 5: is_vowel """
"""
Input: string s
Output: True if s contains at least one character and every char is a vowel
        False otherwise
"""
def is_vowel(s):
    if s=="":
        return False
    has_vowel=False
    for c in s:
        if c in "aeiouAEIOU":
            has_vowel=True
        else:
            return False
    return has_vowel

""" Test 5 """
def test_is_vowel():
    print("Testing is_vowel...", end='')
    assert(is_vowel("") == False)
    assert(is_vowel("a") == True)
    assert(is_vowel("aeiP1") == False)
    assert(is_vowel("ooeai") == True)
    assert(is_vowel("565") == False)
    assert(is_vowel("bcdfgh") == False)
    assert(is_vowel("IOU") == True)
    print("... done!")

if __name__ == '__main__':
    test_is_vowel()