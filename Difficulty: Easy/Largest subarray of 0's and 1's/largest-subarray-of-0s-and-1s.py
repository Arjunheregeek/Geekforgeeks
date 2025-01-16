class Solution:
    def maxLen(self, arr):
        # Replace 0 with -1
        arr = [-1 if x == 0 else 1 for x in arr]
        
        prefix_sum = 0
        hash_map = {}
        max_len = 0
        
        for i, num in enumerate(arr):
            prefix_sum += num
            
            # If prefix_sum is 0, the subarray from 0 to i has equal 0s and 1s
            if prefix_sum == 0:
                max_len = i + 1
            
            # If prefix_sum was seen before, calculate subarray length
            if prefix_sum in hash_map:
                max_len = max(max_len, i - hash_map[prefix_sum])
            else:
                # Store the first occurrence of this prefix_sum
                hash_map[prefix_sum] = i
        
        return max_len

            
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends