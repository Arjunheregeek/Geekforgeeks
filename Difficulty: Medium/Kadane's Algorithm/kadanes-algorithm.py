#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        if len(arr)==1:
            return arr[0]
            
        res=0
        su=0
        for i in arr:
            su=su+i
            if su<0:
                su=0
                continue
            res=max(res,su)
        if res==0:
            return max(arr)
        return res
                
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends