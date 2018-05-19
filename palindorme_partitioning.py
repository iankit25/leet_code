#Given a string s, partition s such that every substring of the partition is a palindrome.

#Return all possible palindrome partitioning of s.

class Solution(object):
	def __init__(self):
		self.palin_list = []

	def check_palin(self,s):
		for i in range((len(s)+1)/2):
			if s[i]!=s[len(s)-1-i]:
				return 0
		return 1

	def palin_strings(self, s, str_list):
		# print s,str_list
		if len(s) == 0 :
			print self.palin_list	
			self.palin_list.append(str_list)
			print self.palin_list
			return
		subs = ''
		for i in range(len(s)):
			subs+=s[i]
			if self.check_palin(subs):
				self.palin_strings(s[i+1:],str_list+[subs])


	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		self.palin_strings(s,[])
		return self.palin_list


obj = Solution()
print obj.partition('aabaa')	
# print obj.check_palin('ababcbababa')
