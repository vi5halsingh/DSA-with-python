class recursion :
    def multiplRecusion(self ,n):
        if n <= 1 :
            return n
        
        last = self.multiplRecusion( n - 1 )
        slast = self.multiplRecusion( n - 2 )
        return last + slast

rec = recursion()
ans = rec.multiplRecusion(8)
print(ans)


# TC : O(2 ** n) :- if we call multiplRecusion(n) - it is goone call two separate fucntion or step and then every single function gonna call its separate two function so the time complexity will be the 2  to the power of n

# SC : O(n) : both values are  not storing simultenuously :last = self.multiplRecusion(n-1) runs completely (its entire sub-tree unwinds and returns) before slast = self.multiplRecusion(n-2) even starts.
# So the stack only ever holds one active path at a time — like a straight line going down, not both branches at once. Once last gets its value, all those stack frames are popped off before the second call begins.
# That's why depth = O(n), not O(2ⁿ). The 2ⁿ is about total number of calls made over time (time complexity), not how many are alive on the stack at once (space complexity).