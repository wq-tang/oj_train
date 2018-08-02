'''
无重复字符的最长子串

给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
'''


'''
思路：用贪心算法来解决，从第一个开始往后遍历，发现有和前面相同的就把当前的长度记录下来 和最大值比较 更新，然后把前面和本字符相同的那一串都丢掉，比如‘eabcdada’
遍历到第二个a的时候长度是5这个时候就把开始的ea舍弃 ，然后开始新的
'''





def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    maxs = 0
    start =0 
    maxs_cur=0
    for i in range(len(s)):
        if s[i] not in s[start:i]:
            maxs_cur+=1
        else:
            if maxs_cur>maxs:
                maxs = maxs_cur
            index = s[start:i].index(s[i])
            maxs_cur = maxs_cur - (index+1)+1
            start = index+start+1

        if maxs_cur>maxs:
            maxs=maxs_cur
    return maxs


#这样的话要比上面的快

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
        """
  
    maxs = 0
    start =0 
    maxs_cur=0
    last = [-1 for i in range(1000)]
    for i in range(len(s)):
        if last[ord(s[i])] < start:
            maxs_cur+=1
        else:
            if maxs_cur>maxs:
                maxs = maxs_cur
            maxs_cur = maxs_cur - (last[ord(s[i])]-start+1)+1
            start = last[ord(s[i])]+1
        last[ord(s[i]) ] = i
    if maxs_cur>maxs:
        maxs=maxs_cur
    return maxs