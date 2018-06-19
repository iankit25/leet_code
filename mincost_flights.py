class Solution(object):
	def __init__(self):
		self.min_cost={}
	def flights_cheap(self, flights_conn, flights_dic,src,dst):
		stops = flights_conn[src]
		if src==dst and len(stops)==0 :
			return 0
		if src!=dst and len(stops)==0:
			self.min_cost[str(src)+"_"+str(dst)] = -1
			return -1
		print self.min_cost
		if str(src)+"_"+str(dst) in self.min_cost.keys():
			return self.min_cost[str(src)+"_"+str(dst)]
		else:
			self.min_cost[str(src)+"_"+str(dst)] = 1e100
		for stop in stops:
			cost = flights_dic[str(src)+"_"+str(stop)] + self.flights_cheap(flights_conn,flights_dic,stop,dst)
		
		if cost<flights_dic[str(src)+"_"+str(stop)]:
			self.min_cost[str(src)+"_"+str(dst)] = -1
		else:
			if cost<self.min_cost[str(src)+"_"+str(dst)]:
				self.min_cost[str(src)+"_"+str(dst)] = cost
		return self.min_cost[str(src)+"_"+str(dst)]

	def findCheapestPrice(self, n, flights, src, dst, K):
		"""
		:type n: int
		:type flights: List[List[int]]
		:type src: int
		:type dst: int
		:type K: int
		:rtype: int
		"""
		flights_dic = {}
		flights_conn ={}
		for i in range(n):
			flights_conn[i]=[]
		for i in range(len(flights)):
			if flights[i][0] in flights_conn.keys():
				flights_conn[flights[i][0]].append(flights[i][1])
			else:
				flights_conn[flights[i][0]] = [flights[i][1]]

			flights_dic[str(flights[i][0])+'_'+str(flights[i][1])] = flights[i][2]
		print flights_conn
		self.flights_cheap(flights_conn, flights_dic, src, dst)
		return self.min_cost[str(src)+"_"+str(dst)]

n = 5
edges =[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2 
dst = 1
k = 1
obj = Solution()
print obj.findCheapestPrice(n,edges,src,dst,k)


