
class Solution:
    def maxWater(self, arr):
        n=len(arr)
        leftm=[0]*n
      
        for i in range(1,n):
            leftm[i] = max(arr[i-1],leftm[i-1])
           
        right=[0]*n
     
        for i in range(n-2,-1,-1):
            right[i] = max(arr[i+1],right[i+1])
        limit=0
        ans=0
        for i in range(n):
            limit=min(leftm[i],right[i])
            if limit>arr[i]:
                limit-=arr[i]
                ans+=limit
                
            
        return ans
            
        
            
            
            
            
            
        
        
        # code here


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends