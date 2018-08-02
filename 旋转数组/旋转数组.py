"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""

"""
思路，如果用一步一步迭代的方法那么 会超时，我们还是用移动之后坐标是 （i+k）%n来解决这个问题
就在原来的数组上迭代。
"""

def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    start = 0
    length = len(nums)
    i = 0
    pre = nums[0]
    if k>0 and length>1 and k!=length:
        for p in range(length):
            i = (i+k)%length
            cur = nums[i]
            nums[i] = pre
            if i == start:
                start+=1
                i+=1
                pre = nums[i]
            else:
                pre = cur

rotate(1,[1,2],2)