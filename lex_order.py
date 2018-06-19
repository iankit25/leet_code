class node:
	def __init__(self,val):
		self.val = val
		self.next = {}

class Solution(object):
	def __init__(self):
		self.head = {}

	def order_trie(self,p,n,val):
		if len(n)==1 :
			# print n
			p[n] = node(val)
			return
		key = n[0]
		self.order_trie(p[key].next,n[1:],val)
		

	def lexicalOrder(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		for i in range(n+1):
			self.order_trie(self.head,str(i),i)

		out = self.print_tree(self.head,[])
		return out
	
	def print_tree(self,head,out):
		for i in range(len(head)):
			if i==0 and len(out)==0:
				continue
			out.append(head[str(i)].val)
			if len(head[str(i)].next) == 0:
				continue
			self.print_tree(head[str(i)].next,out)
		return out

obj = Solution()
print(obj.lexicalOrder(14959))
