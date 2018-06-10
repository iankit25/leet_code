import numpy as np 
class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 0 :
			return 0
		DP = {}
		DP[0] = 0
		DP[1] = 1
		DP[2] = 2
		DP[3] = 3

		for i in range(4,n+1):
			DP[i] = i
			for j in range(1,i):
				tmp = j*j
				if tmp > i:
					break
				DP[i] = min(DP[i],1+DP[i-tmp])
		return int(DP[n])
obj = Solution()
print(obj.numSquares(1))