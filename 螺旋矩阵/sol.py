"""
螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

def spiralOrder(self, matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: List[int]
	"""	
	m = len(matrix)
	if m==0:
		return []
	n = len(matrix[0])
	ans=[]
	def prints(matrix,start,end,ans):

		col = end[1]-start[1]+1
		row = end[0] -start[0] +1
		if col>1 and row>1:
			for i in range(col-1):
				ans.append(matrix[start[0]][start[1]+i])
			for i in range(row-1):
				ans.append(matrix[start[0]+i][end[1]])
			for i in range(col-1):
				ans.append(matrix[end[0]][end[1]-i])
			for i in range(row-1):
				ans.append(matrix[end[0]-i][start[1]])
		elif col ==1:
			for i in range(row):
				ans.append(matrix[start[0]+i][start[1]])
		else:
			for i in range(col):
				ans.append(matrix[start[0]][start[1]+i])

	start = [0,0]
	end = [m-1,n-1]
	while start[0] <= end[0] and start[-1] <=end[-1]:
		prints(matrix,start,end,ans)
		start[0] +=1
		start[1]+=1
		end[0] -=1
		end[1] -=1

	print(ans)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiralOrder(0,matrix)

