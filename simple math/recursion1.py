class recursion :
    def printNameNtimes(self , n , Name , count):
        if int(count) > n : 
            return
        print(Name)
        self.printNameNtimes(n ,  Name, count + 1)
    
    def print1ToN(self ,n,count ):
        if count > n :
            return
        print(count)
        self.print1ToN(n , count + 1)
    
    def Backtracking(selft, n  , c):
        if c > n :
            return
        selft.Backtracking(n, c + 1 )
        print(c)


rec = recursion()
# rec.printNameNtimes(3 , "vishal" , 1)

# rec.print1ToN(5 , 1)

rec.Backtracking(3,1)


# TC : as  steps depends on user input so TC is : O(n)
# SC : also stack is being used n times so SC is also : O(n)
