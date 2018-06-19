import numpy as np
class Solution:
	def __init__(self):
		self.cost_cheap = {}

	def find_cheap(self, flights_dis,flights_conn, src,dst,k):
		stops  = flights_conn[src]
		if src==dst:
			return 0
		else:
			if len(stops) == 0 or k<0:
				return -1
		mincost = 1e100
		for stop in stops:
			cost  = flights_dis[src][stop] + self.find_cheap(flights_dis,flights_conn,stop,dst,k-1)
			if cost < flights_dis[src][stop]:
				continue
			else:
				if mincost > cost:
					mincost =  cost
		return mincost

	def findCheapestPrice(self,n,flights,src,dst,K):
		flights_conn={}
		flights_dis = np.zeros((n,n))
		print flights
		flights_dis[:][:] = -1
		for i in range(n):
			flights_conn[i] = []
		for i in range(len(flights)):
			flights_conn[flights[i][0]].append(flights[i][1])
			flights_dis[flights[i][0]][flights[i][1]] = flights[i][2]
		return int(self.find_cheap(flights_dis,flights_conn,src,dst,K))
n = 10
edges = [[3, 4, 4], [2, 5, 6], [4, 7, 10], [9, 6, 5], [7, 4, 4], [6, 2, 10], [6, 8, 6], [7, 9, 4], [1, 5, 4], [1, 0, 4], [9, 7, 3], [7, 0, 5], [6, 5, 8], [1, 7, 6], [4, 0, 9], [5, 9, 1], [8, 7, 3], [1, 2, 6], [4, 1, 5], [5, 2, 4], [1, 9, 1], [7, 8, 10], [0, 4, 2], [7, 2, 8]]
src = 6
dst = 0
k = 7
obj = Solution()
print obj.findCheapestPrice(n,edges,src,dst,k)