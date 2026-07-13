class ArmstrongChecker:
    def Armstrong_num(n):
        count = len(str(n))
        oldNumber = int(n) 
        sum = 0    
        while oldNumber > 0 :

            digit = oldNumber % 10 
            
            sum += digit ** count
            oldNumber = oldNumber // 10
        return sum == n

number = int(input("enter Number "))

ans = ArmstrongChecker.Armstrong_num(number)
if ans == True :
    print(f"the number {number} is a Armstrong number ")
else :
    print(f"the number {number} is Not a Armstrong number")

