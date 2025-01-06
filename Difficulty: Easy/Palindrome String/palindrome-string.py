#User function Template for python3
class Solution:
    def isPalindrome(self, s: str,i=0,n=None) -> bool:
        
        if n is None:
            n=len(s)-1
        if n<=i:
            return True
        if s[i]==s[n]:
            return self.isPalindrome(s,i+1,n-1)
        else:
            return False
            
            
        
		# code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Use lowercase 's'
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Print "true" or "false"
        print("~")

# } Driver Code Ends