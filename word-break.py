class Solution(object):
	def __init__(self):
		self.DP={}
	def ifbreak(self,s,run_word, wordDict):
		# print s
		# print self.DP			
		if len(s) == 0:
			print run_word
			if run_word in wordDict or len(run_word)==0:
				return True		
			else:
				return False	
			# print run_word
		if run_word in wordDict:
			if s in self.DP.keys():
					return self.DP[s]
			else:
				self.DP[s] =  self.ifbreak(s[1:],s[0],wordDict) or self.ifbreak(s[1:],run_word+s[0],wordDict)
				return self.DP[s]
		else:	
			return self.ifbreak(s[1:],run_word+s[0],wordDict)

	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool`
		"""
		# print wordDict
		return self.ifbreak(s,'',wordDict)
		# return self.DP[s]
obj = Solution()
s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami"
# wordDict = [u'kfomka', u'hecagbngambii', u'anobmnikj', u'c', u'nnkmfelneemfgcl', u'ah', u'bgomgohl', u'lcbjbg', u'ebjfoiddndih', u'hjknoamjbfhckb', u'eioldlijmmla', u'nbekmcnakif', u'fgahmihodolmhbi', u'gnjfe', u'hk', u'b', u'jbfgm', u'ecojceoaejkkoed', u'cemodhmbcmgl', u'j', u'gdcnjj', u'kolaijoicbc', u'liibjjcini', u'lmbenj', u'eklingemgdjncaa', u'm', u'hkh', u'fblb', u'fk', u'nnfkfanaga', u'eldjml', u'iejn', u'gbmjfdooeeko', u'jafogijka', u'ngnfggojmhclkjd', u'bfagnfclg', u'imkeobcdidiifbm', u'ogeo', u'gicjog', u'cjnibenelm', u'ogoloc', u'edciifkaff', u'kbeeg', u'nebn', u'jdd', u'aeojhclmdn', u'dilbhl', u'dkk', u'bgmck', u'ohgkefkadonafg', u'labem', u'fheoglj', u'gkcanacfjfhogjc', u'eglkcddd', u'lelelihakeh', u'hhjijfiodfi', u'enehbibnhfjd', u'gkm', u'ggj', u'ag', u'hhhjogk', u'lllicdhihn', u'goakjjnk', u'lhbn', u'fhheedadamlnedh', u'bin', u'cl', u'ggjljjjf', u'fdcdaobhlhgj', u'nijlf', u'i', u'gaemagobjfc', u'dg', u'g', u'jhlelodgeekj', u'hcimohlni', u'fdoiohikhacgb', u'k', u'doiaigclm', u'bdfaoncbhfkdbjd', u'f', u'jaikbciac', u'cjgadmfoodmba', u'molokllh', u'gfkngeebnggo', u'lahd', u'n', u'ehfngoc', u'lejfcee', u'kofhmoh', u'cgda', u'de', u'kljnicikjeh', u'edomdbibhif', u'jehdkgmmofihdi', u'hifcjkloebel', u'gcghgbemjege', u'kobhhefbbb', u'aaikgaolhllhlm', u'akg', u'kmmikgkhnn', u'dnamfhaf', u'mjhj', u'ifadcgmgjaa', u'acnjehgkflgkd', u'bjj', u'maihjn', u'ojakklhl', u'ign', u'jhd', u'kndkhbebgh', u'amljjfeahcdlfdg', u'fnboolobch', u'gcclgcoaojc', u'kfokbbkllmcd', u'fec', u'dljma', u'noa', u'cfjie', u'fohhemkka', u'bfaldajf', u'nbk', u'kmbnjoalnhki', u'ccieabbnlhbjmj', u'nmacelialookal', u'hdlefnbmgklo', u'bfbblofk', u'doohocnadd', u'klmed', u'e', u'hkkcmbljlojkghm', u'jjiadlgf', u'ogadjhambjikce', u'bglghjndlk', u'gackokkbhj', u'oofohdogb', u'leiolllnjj', u'edekdnibja', u'gjhglilocif', u'ccfnfjalchc', u'gl', u'ihee', u'cfgccdmecem', u'mdmcdgjelhgk', u'laboglchdhbk', u'ajmiim', u'cebhalkngloae', u'hgohednmkahdi', u'ddiecjnkmgbbei', u'ajaengmcdlbk', u'kgg', u'ndchkjdn', u'heklaamafiomea', u'ehg', u'imelcifnhkae', u'hcgadilb', u'elndjcodnhcc', u'nkjd', u'gjnfkogkjeobo', u'eolega', u'lm', u'jddfkfbbbhia', u'cddmfeckheeo', u'bfnmaalmjdb', u'fbcg', u'ko', u'mojfj', u'kk', u'bbljjnnikdhg', u'l', u'calbc', u'mkekn', u'ejlhdk', u'hkebdiebecf', u'emhelbbda', u'mlba', u'ckjmih', u'odfacclfl', u'lgfjjbgookmnoe', u'begnkogf', u'gakojeblk', u'bfflcmdko', u'cfdclljcg', u'ho', u'fo', u'acmi', u'oemknmffgcio', u'mlkhk', u'kfhkndmdojhidg', u'ckfcibmnikn', u'dgoecamdliaeeoa', u'ocealkbbec', u'kbmmihb', u'ncikad', u'hi', u'nccjbnldneijc', u'hgiccigeehmdl', u'dlfmjhmioa', u'kmff', u'gfhkd', u'okiamg', u'ekdbamm', u'fc', u'neg', u'cfmo', u'ccgahikbbl', u'khhoc', u'elbg', u'cbghbacjbfm', u'jkagbmfgemjfg', u'ijceidhhajmja', u'imibemhdg', u'ja', u'idkfd', u'ndogdkjjkf', u'fhic', u'ooajkki', u'fdnjhh', u'ba', u'jdlnidngkfffbmi', u'jddjfnnjoidcnm', u'kghljjikbacd', u'idllbbn', u'd', u'mgkajbnjedeiee', u'fbllleanknmoomb', u'lom', u'kofjmmjm', u'mcdlbglonin', u'gcnboanh', u'fggii', u'fdkbmic', u'bbiln', u'cdjcjhonjgiagkb', u'kooenbeoongcle', u'cecnlfbaanckdkj', u'fejlmog', u'fanekdneoaammb', u'maojbcegdamn', u'bcmanmjdeabdo', u'amloj', u'adgoej', u'jh', u'fhf', u'cogdljlgek', u'o', u'joeiajlioggj', u'oncal', u'lbgg', u'elainnbffk', u'hbdi', u'femcanllndoh', u'ke', u'hmib', u'nagfahhljh', u'ibifdlfeechcbal', u'knec', u'oegfcghlgalcnno', u'abiefmjldmln', u'mlfglgni', u'jkofhjeb', u'ifjbneblfldjel', u'nahhcimkjhjgb', u'cdgkbn', u'nnklfbeecgedie', u'gmllmjbodhgllc', u'hogollongjo', u'fmoinacebll', u'fkngbganmh', u'jgdblmhlmfij', u'fkkdjknahamcfb', u'aieakdokibj', u'hddlcdiailhd', u'iajhmg', u'jenocgo', u'embdib', u'dghbmljjogka', u'bahcggjgmlf', u'fb', u'jldkcfom', u'mfi', u'kdkke', u'odhbl', u'jin', u'kcjmkggcmnami', u'kofig', u'bid', u'ohnohi', u'fcbojdgoaoa', u'dj', u'ifkbmbod', u'dhdedohlghk', u'nmkeakohicfdjf', u'ahbifnnoaldgbj', u'egldeibiinoac', u'iehfhjjjmil', u'bmeimi', u'ombngooicknel', u'lfdkngobmik', u'ifjcjkfnmgjcnmi', u'fmf', u'aoeaa', u'an', u'ffgddcjblehhggo', u'hijfdcchdilcl', u'hacbaamkhblnkk', u'najefebghcbkjfl', u'hcnnlogjfmmjcma', u'njgcogemlnohl', u'ihejh', u'ej', u'ofn', u'ggcklj', u'omah', u'hg', u'obk', u'giig', u'cklna', u'lihaiollfnem', u'ionlnlhjckf', u'cfdlijnmgjoebl', u'dloehimen', u'acggkacahfhkdne', u'iecd', u'gn', u'odgbnalk', u'ahfhcd', u'dghlag', u'bchfe', u'dldblmnbifnmlo', u'cffhbijal', u'dbddifnojfibha', u'mhh', u'cjjol', u'fed', u'bhcnf', u'ciiibbedklnnk', u'ikniooicmm', u'ejf', u'ammeennkcdgbjco', u'jmhmd', u'cek', u'bjbhcmda', u'kfjmhbf', u'chjmmnea', u'ifccifn', u'naedmco', u'iohchafbega', u'kjejfhbco', u'anlhhhhg']
s = "goalspecial"
wordDict = ["go","goal","goals","special"]
print obj.wordBreak(s,wordDict)