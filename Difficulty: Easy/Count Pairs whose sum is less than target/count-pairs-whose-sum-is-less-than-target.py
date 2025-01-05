#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        count = 0
        start, end = 0, len(arr) - 1
        
        while start < end:
            if arr[start] + arr[end] < target:
                
                count += (end - start)
                start += 1 
            else:
                end -= 1 
            
        return count
                    
                
            
            
            
        #Your code here

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends