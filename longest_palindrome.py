import numpy as np 

class Solution(object):
    		
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if len(s)==1:
			return s
		isPalin = np.zeros((len(s),len(s)))
		isPalin[:][:]=2
		long_sub = ''

		for i in range(len(s)-1,-1,-1):
			for j in range(len(s)-1,i-1,-1):
				isPalin[i][j]=0
				if s[i]==s[j]:
					if i!=j and (isPalin[i+1][j-1] == 1 or isPalin[i+1][j-1] == 2):
						isPalin[i][j] = 1
						if j-i+1 > len(long_sub):
							long_sub = s[i:j+1]
					if i==j:
						isPalin[i][j]=1
						if 1 > len(long_sub):
							long_sub = s[i]
		print isPalin
		return  long_sub

obj = Solution()
print obj.longestPalindrome("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        