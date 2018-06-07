import numpy as np
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = np.zeros((m,n))
        # DP[0][0]=1
        for i in range(m):
        	for j in range(n):
        		if i == 0 and j== 0 :
        			DP[i][j]=1
        		elif i == 0 and j!=0:
        			DP[i][j] = DP[i][j-1]
        		elif j==0 and i!=0:
        			DP[i][j] = DP[i-1][j]
        		else:
        			DP[i][j] = DP[i-1][j]+DP[i][j-1]
        return DP[m-1][n-1]

obj = Solution()
print obj.uniquePaths(7,3)