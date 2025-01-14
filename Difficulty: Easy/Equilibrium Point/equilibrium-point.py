# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        l=sum(arr)
        summ=0
        for i in range (1,len(arr)):
            summ+=arr[i-1]
            if summ==(l-arr[i])/2:
                return i 
        return -1
        # code here




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends