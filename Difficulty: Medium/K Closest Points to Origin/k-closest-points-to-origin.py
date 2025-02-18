#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

import heapq
class Solution:
    import heapq
  
        
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        for i in points:
            d=-(i[0]**2+i[1]**2)
            
            heapq.heappush(ans,(d,i))
            if len(ans)>k:
                heapq.heappop(ans)
        return [x for (_,x) in ans]
            
            
        
        # Your code here
        
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends