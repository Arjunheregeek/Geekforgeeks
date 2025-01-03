class Solution:
    def subarrayXor(self, arr, k):
        xor_count = {0: 1}  # Initialize with 0:1 to handle subarrays starting from index 0
        current_xor = 0
        count = 0
    
        for num in arr:
            # Update the current XOR
            current_xor ^= num
            
            # Check if current_xor ^ k exists in the map
            if (current_xor ^ k) in xor_count:
                count += xor_count[current_xor ^ k]
            
            # Update the count of the current_xor in the map
            if current_xor in xor_count:
                xor_count[current_xor] += 1
            else:
                xor_count[current_xor] = 1
        
        return count
        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends