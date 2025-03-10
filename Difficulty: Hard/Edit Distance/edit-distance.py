class Solution:
	def editDistance(self, s1, s2):
       n1,n2=len(s1),len(s2)
       dp=[[None]*(n2+1) for _ in range(n1+1)]
       for i in range(n1+1):
           for j in range(n2+1):
               if i==0:
                   dp[i][j]=j
               elif j==0:
                   dp[i][j]=i
               else:
                   if s1[i-1]==s2[j-1]:
                       dp[i][j]=dp[i-1][j-1]
                   else:
                       dp[i][j]=1+min(dp[i][j-1],
                                        dp[i-1][j],
                                        dp[i-1][j-1])
       return dp[n1][n2]
		# Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1 = input()
        s2 = input()
        ob = Solution()
        ans = ob.editDistance(s1, s2)
        print(ans)
        print("~")

# } Driver Code Ends