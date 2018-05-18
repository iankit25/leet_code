#Given a collection of numbers that might contain duplicates, return all possible unique permutations.
class Solution(object):

	def __init__(self):
		self.unique_perm = {}

	def perm(self,premutation,nums):
		if len(nums) ==0:
			value = [int(x) for x in premutation]
			key = ''.join(premutation)
			self.unique_perm[key] = value
		for i in range(len(nums)):
			num_temp = nums[:i]+nums[i+1:]
			self.perm(premutation+[str(nums[i])],num_temp)

	def permuteUnique(self,nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.perm([],nums)
		output = self.unique_perm.values()
		return output

obj = Solution()
a = obj.permuteUnique(['2','3','2','-1'])
print a