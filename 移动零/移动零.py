'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

思路： 从前往后遍历 遇到0一个0之后记录继续往后遍历，之后每个数向前一步走，继续遇到0记录遇到了m个0 那么之后的每个数往前走m步。



解法1：递归的解法，，要定义全局变量
'''
def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    global count
    count = 0
    def fun(nums,i):
        global count
        for k in range(i,length):
            if nums[k] != 0:
               nums[k-count] = nums[k]
            else:
                count+=1
                fun(nums,k+1)
                break
    fun(nums,0)
    for i in range(length-count,length):
        nums[i]=0
   

#解法2 非递归  维护index

def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    index = 0
    length=len(nums)
    for i in range():
    	if nums[i]!=0:
    		nums[index] = nums[i]
    		index+=1

    for i in range(index,length):
        nums[i]=0 