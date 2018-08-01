def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ans=[]
    hash_table = {}
    for i in range(len(nums)):
    	hash_table[nums[i]] = i

    for i in range(len(nums)):
    	delta = target - nums[i]
    	if delta in hash_table and hash_table[delta] != i:
    		ans.append(i)
    		ans.append(hash_table[delta])
    return ans
