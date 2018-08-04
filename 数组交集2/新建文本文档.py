class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        record, result = {}, []
        for num in nums1:
            record[num] = record.get(num, 0) + 1

        for num in nums2:
            if num in record and record[num]:
                result.append(num)
                record[num] -= 1
        return result

'''
在python中map的底层实现是通过hash表实现的，所以添加元素和搜索元素的时间复杂度都是O(1)级别的，
那么上述的算法时间复杂度是O(n)这个级别的。而空间复杂度依旧是O(n)级别的。如果要使用有序的map，
就要使用collections.OrderedDict。



给定两个数组，写一个方法来计算它们的交集。

例如:
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

注意：

   输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
   我们可以不考虑输出结果的顺序。
跟进:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？

'''