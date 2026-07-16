class recursion :
    def printNameNtimes(self , n , Name , count):
        if int(count) > n : 
            return
        print(Name)
        self.printNameNtimes(n ,  Name, count + 1)

rec = recursion()
rec.printNameNtimes(3 , "vishal" , 1)


# TC : as  steps depends on user input so TC is : O(n)
# SC : also stack is being used n times so SC is also : O(n)
