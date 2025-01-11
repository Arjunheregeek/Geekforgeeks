#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        start = 0
        maxlen = 0  # Set to 0 to handle edge cases (like an empty string)
        end = 0

        while end < len(s):
            # Check if the current window contains unique characters
            k = list(s[start:end + 1])
            if len(set(k)) == len(k):
                maxlen = max(maxlen, end - start + 1)  # Update max length
                end += 1  # Expand the window
            else:
                start += 1  # Shrink the window by moving the start pointer

        return maxlen

                
                
    
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends