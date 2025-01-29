#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
class Solution:
    def power(self, b, e):
        if e == 0:
            return 1  # Base case: any number to power 0 is 1
        
        if e < 0:
            return 1 / self.power(b, -e)  # Convert negative exponent to positive
        
        half = self.power(b, e // 2)  # Recursive call for half exponent
        
        if e % 2 == 0:
            return half * half  # If exponent is even, multiply the half results
        else:
            return b * half * half  # If exponent is odd, multiply one more base
        
        # Code Here

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends