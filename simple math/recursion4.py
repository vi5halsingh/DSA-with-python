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


rec = recusion()
arrNew = []
rec.subSequentEqualToSum([1, 2 , 1] , 0 , 3 , arrNew , 0 , 2)

# TC  : O(2 ** n)
# SC : O(n)