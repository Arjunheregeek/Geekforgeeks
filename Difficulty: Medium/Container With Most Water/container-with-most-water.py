
class Solution:
    def maxWater(self, arr):
        # Initialize two pointers
        left = 0
        right = len(arr) - 1
        
        # Variable to store the maximum water
        max_water = 0
        
        # Use the two-pointer approach
        while left < right:
            # Calculate the width and height of the container
            width = right - left
            height = min(arr[left], arr[right])
            
            # Calculate the water held and update max_water
            max_water = max(max_water, width * height)
            
            # Move the pointer pointing to the smaller height
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
        
        
        
        
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