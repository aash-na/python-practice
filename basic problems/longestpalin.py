def longest_palindrome(s):
    result = ""
    
    for i in range(len(s)):
        temp = expand(s, i, i)
        if len(temp) > len(result):
            result = temp
        
        temp = expand(s, i, i + 1)
        if len(temp) > len(result):
            result = temp

    return result

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


s = input("Enter a string: ")
print("Longest palindrome:", longest_palindrome(s))