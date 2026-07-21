class recusion :
    def subSequentOF(self , arr , i , n, arrNew):

        if i >= n :
            print(arrNew)
            return
        arrNew.append(arr[i])
        
        self.subSequentOF(arr , i + 1 , n, arrNew)

     
        arrNew.pop()
        
        self.subSequentOF(arr , i + 1 , n , arrNew)

    def subSequentEqualToSum(self , arr , i , n, arrNew , s , sum):

        if i == n :
            if s == sum :
                print(arrNew)
            return
        
        arrNew.append(arr[i])

        s = s + arr[i]
        
        self.subSequentEqualToSum(arr , i + 1 , n, arrNew ,  s , sum)

        arrNew.pop()

        s = s - arr[i]
        
        self.subSequentEqualToSum(arr , i + 1 , n , arrNew ,  s , sum)

    def returnOnlyOneStringEqualToSum(self , n , i , arr , newArr , s  ,sum):
        if i == n :
            if sum == s :
                print(newArr)
                return True
            else : return False

        
        newArr.append(arr[i])

        sum = sum + arr[i]

        if self.returnOnlyOneStringEqualToSum( n , i + 1  , arr , newArr , s  ,sum) :
            return newArr

        newArr.pop()

        sum = sum - arr[i]

        if self.returnOnlyOneStringEqualToSum( n , i + 1, arr , newArr , s  ,sum) :
            return newArr
        
        return False





rec = recusion()
arrNew = []
rec.returnOnlyOneStringEqualToSum(4 , 0 ,[2 , 5 , 1 , 8] , arrNew , 8 , 0)


# TC  : O(2 ** n)
# SC : O(n)