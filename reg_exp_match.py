#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'
class Solution(object):
	def check_star(self,p,preceeding_ele):
		print p
		for i in range(len(p)):
			if p[i] == '*':
				continue
			else:
				if i+1== len(p):
					return False
				else:
					if p[i+1] == '*':
						continue
					else:
						return False
		return True

	def check_match(self,s,p,i,preceeding_ele):
		if len(s)==0:
			if i<len(p):
				return self.check_star(p[i:],'')
			return True
		if i>=len(p):
			return False
		if s[0] == p[i]:
			return self.check_match(s[1:],p,i+1,s[0]) or self.check_match(s,p,i+1,s[0])
		elif p[i] == '*':
			if s[0]== preceeding_ele or preceeding_ele =='.':
				return self.check_match(s[1:],p,i,s[0]) or self.check_match(s,p,i+1,preceeding_ele)
			else:
				return self.check_match(s,p,i+1,preceeding_ele)
		elif p[i] =='.':
			return self.check_match(s[1:],p,i+1,'.')
		else :
			return self.check_match(s,p,i+1,p[i])
		# return False




	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""

		out = self.check_match(s,p,0,'')
		return out
obj = Solution()
s = "mississippi"
p = "mis*is*p*."
print obj.isMatch(s,p)
        