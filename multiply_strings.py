#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
import math

class Solution(object):
	def make_length_equal(self,num1,num2):
		if len(num1)>len(num2):
			diff = len(num1) - len(num2)
			for i in range(diff):
				num2+='0'
		else:
			diff = len(num2) - len(num1)
			for i in range(diff):
				num1='0'+num1
		return num1,num2

	def add_strings(self,num1,num2):
		added_number = ''
		if len(num1)!= len(num2):
			num1,num2 = self.make_length_equal(num1,num2)
		carry = 0
		for i in range(len(num1)-1,-1,-1):
			add = ord(num1[i])+ord(num2[i])-2*ord('0')
			num = (carry + add)%10
			carry = (carry + add)/10
			added_number = str(num)+added_number
		if carry != 0:
			added_number = str(carry)+added_number
		return added_number

	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		output = '0'
		for i in range(len(num1)-1,-1,-1):
			ele1 = ord(num1[i])-ord('0')
			# print ele1
			carry = 0
			multiplied_num = ''
			for j in range(len(num2)-1,-1,-1):
				ele2 = ord(num2[j])-ord('0')
				mul = ele1 * ele2
				num = (carry+mul)%10 
				carry = (carry+mul)/10
				multiplied_num = str(num)+multiplied_num
			if carry !=0:
				multiplied_num = str(carry)+multiplied_num
			for k in range(len(num1)-i-1):
				multiplied_num = multiplied_num+'0'
			# print multiplied_num
			output = self.add_strings(output,multiplied_num)
		if ord(output[0]) == ord('0'):
			return '0' 
		return output

obj = Solution()
print obj.multiply("140","72")
