"""Write a Python function that checks whether
a given string is a palindrome. A palindrome
is a word, phrase, or sequence that reads the
same backward as forward (e.g.,

"madam" or

"racecar")."""

def is_palindrome(s):
    str = ''.join(s.split()).lower()
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("racecar"))
