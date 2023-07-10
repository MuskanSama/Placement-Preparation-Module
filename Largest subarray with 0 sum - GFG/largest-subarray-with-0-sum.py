#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        sumMap = {}
        maxLen = 0
        totalSum = 0
    
        for i in range(n):
            totalSum += arr[i]
    
            if totalSum == 0:
                maxLen = i + 1
    
            if totalSum in sumMap:
                maxLen = max(maxLen, i - sumMap[totalSum])
            else:
                sumMap[totalSum] = i
    
        return maxLen



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends