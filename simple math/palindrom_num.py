def palidrom_num(n):
    oldvalue = n
    rev = 0
    while(n > 0 ):

        rev = (rev * 10) + (n % 10)

        n  = int(n / 10)
    
    print(rev)

    if oldvalue == rev :
        print(oldvalue, "is palindrom")
    else : print("not a palindrom number")

palidrom_num(1221)