class divisors:
    def findDivisor(n):
       
        divisors = []
        i = 1
        while i*i <= n :
            if n % i == 0:
                divisors.append(i)
                if i != n // 2:
                    divisors.append(n // i)
            i += 1
        return divisors      
Number = 30
ans = divisors.findDivisor(Number)
print(ans)



# TC = O(n)
#space = O(n)