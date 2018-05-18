#The gray code is a binary numeral system where two successive values differ in only one bit.

#Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
import math
class Solution(object):
	def __init__(self):
		self.gray_code = []

	def decimal_equiv(self,num_list):
		gray_code = []
		for num in num_list:
			out = 0
			for i in range(len(num)):
				out+= int(num[len(num)-1-i])*int(math.pow(2,i))
			gray_code.append(out)
			# print gray_code
		return gray_code

	def binary_num(self,n,num_list):
		if n == 0:
			self.gray_code =  self.decimal_equiv(num_list)
			return
		zero_add,one_add = [],[]
		for ele in num_list:
			zero_add.append('0'+ele)
			one_add.insert(0,'1'+ele)
		num_list = zero_add+one_add
		# print num_list,n-1
		self.binary_num(n-1,num_list)


	def grayCode(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		if n==0:
			return [0]
		self.binary_num(n-1,['0','1'])
		return self.gray_code

obj = Solution()
print obj.grayCode(2)