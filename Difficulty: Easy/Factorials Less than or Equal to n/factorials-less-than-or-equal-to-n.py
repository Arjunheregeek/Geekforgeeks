#User function Template for python3
class Solution :
    
    def factorialNumbers(self, n, fact=1, i=1):
            # Base case: If the current factorial exceeds n, stop recursion
            if fact > n:
                return []
            
            # Recursive case: Include the current factorial and compute the next
            return [fact] + self.factorialNumbers(n, fact * (i + 1), i + 1)
            
        

        
            
    	#code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends