#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, nums, k):
        
       r= k % len(nums)      
       # Get the number of elements to move from the end to the beginning
      
       # Store the elements to move
       new = nums[0:r]
       # Remove the elements from the beginning
       nums[0:r] = []
       # Append the stored elements to the end
       nums.extend(new)
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends