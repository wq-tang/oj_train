
#1.生成长度为N(arr的长度)的数组dp，dp[i]表示在以arr[i]结尾的情况下，arr[0…i]中的最长子序列。
#2.dp的初始值是1也是边界条件
#3.dp[i] = max(dp[j]+1,dp[i]) ,j in [0..i]
#o(n^2)

def subseq(data):
	lenghth = len(data)
	dp = [1 for i in range(lenghth)]
	for i in range(lenghth):
		for j in range(i):
			if data[j]<data[i]:
				dp[i] = max(dp[j]+1,dp[i])
	
	return max(dp)

def subseq_log(data):
	def replace(dp,k):
		left = 0
		right = len(dp)-1
		while left<right:
			middle = (left+right)//2
			if k==dp[middle]:
				return 
			elif k<dp[middle]:
				right=middle
			else:
				left = middle+1
		dp[right] = k

	lenghth = len(data)
	dp = [data[0]]
	for i in range(1,lenghth):
		item = data[i]
		if data[i]>dp[-1]:
			dp.append(data[i])
		else:
			replace(dp,data[i])
	print(dp)
	return len(dp)



if __name__=='__main__':
	array = [13,7,8,16,21,4,18,7,90,2,3,4,34,56,11,2]
	print(subseq(array))
	print(subseq_log(array))
