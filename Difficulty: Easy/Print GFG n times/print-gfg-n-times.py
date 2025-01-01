#User function Template for python3

class Solution:
    def printGfg(self, n):
        if n==0:
            return 
        else:
            print ("GFG",end=" ")
            n-=1
            return self.printGfg(n)
            
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
        print("~")
# } Driver Code Ends