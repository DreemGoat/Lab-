def emirpCheck(x):
    reversed = 0
    num = x
    if num > 9:
        for i in range(2,num//2):
            if (num % i) == 0:
                print("False!")
                return False
                break
        else:
            while num != 0:
                digit = num %10
                reversed = reversed * 10  + digit
                num=num//10
            for k in range(2,reversed//2):
                if (reversed % k) ==0:
                    print("False!")
                    return False
                    break
            else:
                print(x, reversed, sep=" ")
                return True
    else:
        print("False!")
        return False
emirpCheck(13)
emirpCheck(347)
emirpCheck(5)