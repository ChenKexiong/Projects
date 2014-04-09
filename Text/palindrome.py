# palindrome
s = raw_input('Input a string:\n').lower()
if s == s[::-1]:
    print 'This string is a palindrome'
else:
    print 'This string is not a palindrome'
