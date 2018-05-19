#Given a 2D board and a word, find if the word exists in the grid.
class Solution(object):
	def find_start(self,board,alpha):
		locations = []
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == alpha:
					locations.append([i,j])
		return locations

	def find_next_locations(self,loc,row,col,hitlist):
		i,j = loc[0],loc[1]
		next_loc = []
		if i+1 < row:
			next_loc.append([i+1,j])
		if j+1<col:
			next_loc.append([i,j+1])
		if i-1>=0:
			next_loc.append([i-1,j])
		if j-1>=0:
			next_loc.append([i,j-1])
		to_remove = []
		for k in range(len(next_loc)):
			if next_loc[k] in hitlist:
				to_remove.append(k)	
		for k in range(len(to_remove)):
			next_loc.pop(to_remove[len(to_remove)-1-k])	
		return next_loc

	def if_exist(self, loc, board, word,hitlist):
		if len(word) == 0:
			return 1
		next_loc = self.find_next_locations(loc,len(board),len(board[0]),hitlist)
		if len(next_loc) == 0:
			return 0
		flag = 0
		for ele in next_loc:
			if board[ele[0]][ele[1]] == word[0]:
				flag = flag or self.if_exist(ele,board,word[1:],hitlist+[ele])
		return flag

	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""

		start_location = self.find_start(board,word[0])
		print start_location
		for loc in start_location:
			hitlist = [loc]
			if self.if_exist(loc, board, word[1:],hitlist):
				return True
		return False

obj = Solution()
board =[["a"]]
print obj.exist(board, 'ab')

