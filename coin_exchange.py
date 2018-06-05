class Solution(object):

	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		Count_coins = [1e100 for i in range(amount+1)]
		Count_coins[0] = 0
		for i in range(1,amount+1):
			for coin in coins:
				if coin <=i:
					tmp = Count_coins[i-coin]
					if tmp!=1e100and tmp<Count_coins[i]:
						Count_coins[i] = tmp+1
		# print Count_coins
		if Count_coins[amount] == 1e100:
			return -1
		return Count_coins[amount]


obj = Solution()
print obj.coinChange([1,2,5],30)

        