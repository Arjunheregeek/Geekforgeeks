#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        res=[]
        start=0
        sum=0
        
        for end in range (0,len(arr)):
            sum=sum+arr[end]
            
            if sum<target:
                continue 
            elif sum>target:
                while sum>target:
                    sum=sum-arr[start]
                    start+=1
               
                
                
            if sum == target :
                return [start+1,end+1]
        return [-1]
                
                
            
            
            
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends