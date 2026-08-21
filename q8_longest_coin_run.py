""" Question 8: longest_coin_run """
"""
Input: string s of Hs and Ts
Output: the length of the longest run of Hs or Ts
"""


def longest_coin_run(s):
    value='a'
    count=0
    high=1
    for c in s:
        if value!=c:
            count=0
            count+=1
            value=c
        else:
            count+=1

        if high<count:
            high=count
    return high

""" Test 8 """
def test_longest_coin_run():
    print("Testing longest_coin_run...", end='')
    assert(longest_coin_run('H') == 1)
    assert(longest_coin_run('HTT') == 2)
    assert(longest_coin_run('HHHH') == 4)
    assert(longest_coin_run('HT') == 1)
    assert(longest_coin_run('HHTTTTHH') == 4)
    print("... done!")


if __name__ == '__main__':
    test_longest_coin_run()