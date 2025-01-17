#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        k=len(arr)
        left=[1]*k
        right=[1]*k
        res=[]
        
        for i in range(k-2,-1,-1):
            right[i]=right[i+1]*arr[i+1]
        for i in range(1,k):
            left[i]=left[i-1]*arr[i-1]
            right[i]=right[i]*left[i]
        return right
        
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends