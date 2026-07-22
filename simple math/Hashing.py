

class Hashing :
    def findThElementCout(self , arr, newArr ,quary ):
         
        for i in range(0 , len(arr)) :
            newArr[arr[i]] += 1

        return newArr

hash = Hashing()

arr = [1 , 1, 2, 3 ,5]
newArr = [0] * 12

ans = hash.findThElementCout(arr,newArr , 1)
print(ans)


# Time complexity : o(n)
#  space complexity : O(n)

#  more : if there is huge amount of element in an array like 10 to the powere 9 then we will have to calculate for 10 to the power of 9 plus 1 (10 ** 9 + 1) so we will get elements till last index

#  but there is a pre limit for array memory search for it if int array and inside a block or inside main  limit 10 ** 6 and if boolean then 10 ** 7 
#  if int array and is a global array then  limit 10 ** 7 and if boolean then 10 ** 8 