'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''

'''
要求
题目比较好理解，但是有几个关键点这里需要明确一下：

不能用除法。意思就是：你不能上来先把所有数乘积算出来，然后再逐个除以每个元素，这种思路是无聊、没技术含量而且不被允许的。
时间复杂度必须控制到O(n)。意思是：如果用O(n^2)的方法，那外层一个for循环，内层左右遍历就解决了，也是很无聊的解法。
空间复杂度最好是常数，但是重新分配的返回数组不算在内。
思路1
我们以一个4个元素的数组为例，nums=[a1, a2, a3, a4]。 
想在O(n)时间复杂度完成最终的数组输出，res=[a2*a3*a4, a1*a3*a4, a1*a2*a4, a2*a3*a4]。

比较好的解决方法是构造两个数组相乘：

[1, a1, a1*a2, a1*a2*a3]
[a2*a3*a4, a3*a4, a4, 1]
这样思路是不是清楚了很多，而且这两个数组我们是比较好构造的。
类似马尔可夫前后向算法
'''

def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    length = len(nums)
    one = [0 for i in range(length)]
    two = [0 for i in range(length)]
    one[0] = 1
    two[-1] =1
    for i in range(1,length):
    	one[i] = nums[i-1]*one[i-1]
    	
    for i in range(1,length):
    	two[length -i-1] = two[length-i]*nums[length-i]

    for i in range(length):
    	two[i] = one[i]*two[i]
    return two

#数空间复杂度
def method2(nums):
	forward = 1
	output = [0 for i in range(len(nums))]
	output[0] = 1
	for i in range(1,len(nums)):
		output[i] = nums[i-1] *output[i-1]
	for i in range(1,len(nums)+1):
		output[len(nums)-i] *= forward
		forward *= nums[len(nums)-i] 
	return output 

