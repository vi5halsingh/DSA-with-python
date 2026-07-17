class recursion :
    def reverseArray(self , arr , l , r ):
        if l >= r :
            return arr
       
        temp = arr[l] 
        arr[l] = arr[r] 
        arr[r] = temp

        return self.reverseArray(arr,l = l+1 , r = r-1)
    
    def reverseArrayONeVariable(self , arr , i ):
        if i >= len(arr)- i - 1 :
            return arr
   
        temp = arr[i] 
        arr[i] = arr[len(arr)- i - 1] 
        arr[len(arr)-1 - i] = temp
        return self.reverseArrayONeVariable(arr, i = i + 1)

obj = recursion()
arr = [5,4,3,2,1]
l = 0
r = len(arr) - 1
ans = obj.reverseArrayONeVariable(arr , 0)
print(ans)



# TC : o(n)
# TC : o(n)