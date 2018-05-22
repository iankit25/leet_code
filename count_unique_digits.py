#Given a non-negative integer n, count all numbers with unique digits, x,

class Solution(object):
	def __init__(self):
		self.unique_count = {}

	def count(self,n,num,num_list):
		if n == 0 :
			return 
		j = 0
		for i in num_list:
			j+=1
			key =num+str(i)
			self.unique_count[key] = 1
			if key[0]!='0':
				self.count(n-1,num+str(i),num_list[:j]+num_list[j+1:])
			


	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		self.count(n,'',[0,1,2,3,4,5,6,7,8,9])
		print self.unique_count.keys()
		return len(self.unique_count.keys())
		
obj = Solution()
print obj.countNumbersWithUniqueDigits(2)