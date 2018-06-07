import numpy as np
class Solution1(object):
	def checkSubarraySum(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		sum_upto = np.zeros((len(nums),len(nums)))
		for i in range(len(nums)):
			sum_upto[i][i] = nums[i]
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				sum_upto[i][j] = sum_upto[i][j-1]+nums[j]
				if k == 0:
					if j-i+1>=2 and sum_upto[i][j] == 0:
						return True
				else:
					if sum_upto[i][j] % k ==0 and j-i+1>=2:
						return True
		return False

obj = Solution1()
print obj.checkSubarraySum([1],  1)

class Solution2(object):
	def checkSubarraySum(self, nums, k):
		run_sum = 0
		prev = []
		count = 0
		for i in range(len(nums)):
			run_sum+=nums[i]
			if k!=0:
				run_sum%=k
				if nums[i]!=0 and run_sum==0 and i>=1:
					return True
				indices = [l for l, x in enumerate(prev) if x == run_sum]
				if indices:
					for j in indices:
						print i,j
						if i-j+1>=2:
							return True
				else:
					prev.append(run_sum)
			else:
				if nums[i]==0:
					count+=1
				else:
					count = 0
				if count>=2:
					return True

		return False


obj = Solution2()
print obj.checkSubarraySum([1],  1)
