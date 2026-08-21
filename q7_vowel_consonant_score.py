
from q5_is_vowel import is_vowel
from q6_is_consonant import is_consonant


def vowel_consonant_score(s):
    vowel_count=0
    consonant_count=0
    for c in s:
        if is_vowel(c):
            vowel_count+=1
        elif is_consonant(c):
            consonant_count+=1
    if consonant_count>0:
        score=vowel_count/consonant_count
        score=round(score)
    else:
        score=0
    return score

""" Test 7 """
def test_vowel_consonant_score():
    print("Testing vowel_consonant_score...", end='')
    assert(vowel_consonant_score("") == 0)
    # assert(vowel_consonant_score("aeioub") == 5)
    assert(vowel_consonant_score("aeiPl") == 2)
    assert(vowel_consonant_score("bcdfgh") == 0)
    assert(vowel_consonant_score("86AAABBB") == 1)
    assert(vowel_consonant_score("AEIOU") == 0)
    assert(vowel_consonant_score("Blckaaeeeiii") == 2)
    assert(vowel_consonant_score("How are you?") == 1)
    print("... done!")

if __name__ == '__main__':
    test_vowel_consonant_score()