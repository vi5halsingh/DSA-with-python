class recusion :
    def subSequentOF(self , arr , i , n, arrNew):

        if i >= n :
            print(arrNew)
            return
        arrNew.append(arr[i])
        
        self.subSequentOF(arr , i + 1 , n, arrNew)

     
        arrNew.pop()
        
        self.subSequentOF(arr , i + 1 , n , arrNew)

rec = recusion()
arrNew = []
rec.subSequentOF([3,1,2] , 0 , 3 , arrNew)

# TC  : O(2 ** n)
# SC : O(n)