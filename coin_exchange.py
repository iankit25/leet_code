class Solution(object):
	def __init__(self):
		self.Count_coins = {}

	def Min_coins(self,coins, amount):
		# raw_input()
		L = len(coins)
		if L == 0  or amount < 0:
			return 1e100
		if amount == 0 :
			self.Count_coins[str(amount)] = 0
			return self.Count_coins[str(amount)]
		else:
			if amount in self.Count_coins.keys():
				return self.Count_coins[str(amount)]
			else:
				self.Count_coins[str(amount)] = min(1+self.Min_coins(coins,amount-coins[L-1]),self.Min_coins(coins[:L-1],amount))
				return self.Count_coins[str(amount)]


	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		self.Min_coins(coins,amount)
		if self.Count_coins[str(amount)] >=1e100:
			return -1
		return self.Count_coins[str(amount)]
obj = Solution()
print obj.coinChange([5,2,1],30)

        