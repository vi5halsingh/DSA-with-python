class PrimeNumberCheker:
    def isPrime(n):
        i = 2
        while i * i <=n :
            if n % i == 0 :
                return False
            i += 1
        return True

number = int(input("enter the number to check : "))
print(PrimeNumberCheker.isPrime(number))

# TC is sqrt of N 
# SC is O(1)