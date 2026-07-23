class Hasing :
    def StringOP(self , target , string , newArr):

        targetIndex = ord(target) - ord("a")
        for ch in string :
            index = ord(ch) - ord("a")

            if index == targetIndex :
                newArr[targetIndex] += 1  
            
        return newArr[targetIndex]


    def checkIterationInString(self , string) :

        disk = {}

        for ch in string :
            if ch in disk : 
                disk[ch] += 1
            else :
                disk[ch] = 1

        return disk

hash = Hasing()

s = "aanandi"

newarr = [0] * 26

print(hash.StringOP("n", s ,  newarr))


# time complexity is : O(1)
# space complexity is : O(1)



