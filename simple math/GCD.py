def GCD(n1 , n2):
    minLengh = min(n1,n2)
    gcd = 1
    i = 1
    while(i < minLengh):
        rn1 =  n1 % i 
        rn2 = n2 % i 
        if rn1 == 0 and rn2 == 0 :
            if gcd < i :
                gcd = i
        i = i + 1
    print(gcd)
GCD(20,15)




