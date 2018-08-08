'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''

'''
解法一：思路很简单和前面的硬币那个差不多https://blog.csdn.net/wqtltm/article/details/81430004，就不多说了，这里我主要想用用生成器。时间复杂度o(n^1.5)
'''

def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    import math
    def generator(n):
    	x=1
    	while x<math.sqrt(n):
    		yield x**2
    		x+=1
    nums = [n+1 for i in range(n+1)]
    nums[0]=0
   
    for i in range(n+1):
    	if nums[i]<n+1:
            gen = generator(n)
            for value in gen:
                if i+value<=n:
                    nums[i+value] = min(nums[i+value],nums[i]+1)
                    


    return nums[-1]

'''
解法二：解法一，虽然可行也很高效，但是针对平方数这么有特点的数肯定不是 最优的解法，最优的解法用到了四平方和定理
根据四平方和定理，任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和，那么就是说返回结果只有1,2,3或4其中的一个，
首先，一个数如果可以整除4那么 这个数除以四之后得到的那个数和这个数得到的结果是相同的，也就是说64和16，16和4返回的结果都相同，具体证明我也不会

还有一个可以化简的地方就是，如果一个数除以8余7的话，那么肯定是由4个完全平方数组成，并且所有由4平方组成的数都有余7的特性。这个我也不会证明
那我们发现余4的数字解决了，下面我们就来尝试的将其拆为两个平方数之和，如果拆成功了那么就会返回1或2，代码的int(y>0)+int(x>0)表示两个都不为0就返回2，否则是1，他们是不可能同时为0的
最后剩余的就是3了。。。。。。怎么说呢，数学味道太浓了   渣渣我要哭了。 时间复杂度o(n)
看代码
'''
def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    import math
    while n%4==0:
        n/=4
    if n%8==7:
        return 4
    for x in range(int(math.sqrt(n))+1):
        y = int(math.sqrt(n-x**2))
        if y**2+x**2==n:
            return int(y>0)+int(x>0)
    return 3
