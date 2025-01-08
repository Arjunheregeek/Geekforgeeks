#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        n = len(arr)
        arr.sort()  # Sort the array to use the triangle property effectively
        count = 0
    
        # Fix the third side (largest side) as arr[k]
        for k in range(2, n):
            start = 0
            end = k - 1
    
            # Use two-pointer technique to find valid pairs for arr[k]
            while start < end:
                # Check if arr[start] + arr[end] > arr[k]
                if arr[start] + arr[end] > arr[k]:
                    # All pairs from start to end are valid
                    count += (end - start)
                    end -= 1  # Move the end pointer left
                else:
                    start += 1  # Move the start pointer right
    
        return count

            
            
            
        
       
            
        
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends