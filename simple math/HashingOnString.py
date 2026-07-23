class Hasing :
    def StringOP(target , string , newArr, c ):
        for i in range(0 , len(string)):
            if newArr[string[i] - target ] == target :
                c += 1
        return c



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

# newarr = [0] * 26

print(hash.checkIterationInString(s))

# hash.StringOP("a", "abradsa" , [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0)

