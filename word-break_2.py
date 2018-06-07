import numpy as np
class Solution:

	def wordBreak(self,s,wordDict):
		DP = np.zeros(len(s)+1)
		DP[-1] = 1
		for i in range(len(s)-1,-1,-1):
			for word in wordDict:
				if s[i-len(word)+1:i+1] ==word and DP[i+1]==1:		
					DP[i-len(word)+1] = 1
		if DP[0] == 1:
			return True
		else:
			return False
obj = Solution()
print obj.wordBreak("leetcode",["leet","code"])