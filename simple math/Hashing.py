

class Hashing :
    def findThElementCout(self , arr, newArr ,q):
         
        for i in range(0 , len(arr)) :
            newArr[arr[i]] = newArr[arr[i]] + 1

        return newArr[q]

hash = Hashing()

arr = [1 , 1, 2, 3 ,5]
newArr = [0] * 12

ans = hash.findThElementCout(arr,newArr , 1)
print(ans)