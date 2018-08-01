 def jump(self, nums):
    length = len(nums)
    pre_maxsize=0
    cur_maxsize = 0
    count = 1
    if length == 1:
        return 0
    for i in range(0,len(nums)):
        cur_maxsize = max(nums[i]+i,cur_maxsize)
        if cur_maxsize >=length-1:
            return count
        if i==pre_maxsize:
            pre_maxsize = cur_maxsize
            count+=1

        