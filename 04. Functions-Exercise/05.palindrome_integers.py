def isPalindrome(s):
    return s == s[::-1]


my_list = input()
my_list = my_list.split(", ")
for x in my_list:
    print(isPalindrome(x))