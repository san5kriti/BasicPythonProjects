#palindrome checker, checks if a word is a palindrome or not
#What is a palindrom? Words that are spelt the same from both backwards and frontwards, example
#- 'kayak', 'noon'.

#Method 1: Slicing Operation
def palindromchecker1(s):
    return s == s[::-1]

s = input("enter a word ")
ans = palindromchecker1(s)

if ans: 
    print("yes")
else:
    print("no")
    
#Method 2: Loop to compare letters
def is_palindrome2(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

s = input("Enter a word: ")
if is_palindrome2(s):
    print("Yes")
else:
    print("No")

#Method 3: Using 'reversed()' function
def is_palindrome3(s):
    return s == ''.join(reversed(s))

s = input("Enter a word: ")
if is_palindrome3(s):
    print("Yes")
else:
    print("No")


#Method 4: Using recursive function
def is_palindrome4(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome4(s[1:-1])

s = input("Enter a word: ")
if is_palindrome4(s):
    print("Yes")
else:
    print("No")
