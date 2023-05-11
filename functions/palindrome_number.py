def palindrome_number(num):
    temp = num
    reverse = 0
    while(num>0):
        dig = num%10
        reverse = reverse*10 + dig
        num = num//10

    if temp == reverse:
        return True
    else:
        return False
