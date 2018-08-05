'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
'''



'''
这个是个简答的动态规划，用mins【i】表示 凑i面值至少需要的硬币数目。
'''
#解法1，这样做出来复杂度o(n^2)
def coinChange(self, coins, amount):
	"""
	:type coins: List[int]
	:type amount: int
	:rtype: int
	"""
	if amount==0:
		return 0
	mins = [-1 for i in range(amount+1)]
	if amount in coins:
		return 1
	for i in range(1,amount+1):
		if i in coins:
			mins[i] = 1
			continue
		if i>1:
			m = amount+1
			for j in range(1,int(i/2)+1):
				if mins[i-j]>0 and mins[j]>0:
					m = min(m,mins[i-j]+mins[j])
			if m <=amount:
				mins[i] =m
	return mins[-1]


#解法2 优化：因为往往硬币的面值会小于需求的面值，m是硬币种类数，n是面值。因此往往m《《n。所以现在这么做复杂度是o(mn)这样做是更好的。但是python太慢了还是通不过case

def coinChange2(self, coins, amount):
	"""
	:type coins: List[int]
	:type amount: int
	:rtype: int
	"""
	mins = [amount+1 for i in range(amount+1)]
	mins[0] = 0
	for i in range(amount+1):
		if mins[i] <=amount:
			for coin in coins:
				if i+coin<=amount:
					mins[i+coin] = min(mins[i+coin],mins[i]+1)

	if mins[-1] <=amount:
		return mins[-1]
	else:
		return -1

coinChange2(1,[1,2,3],11)