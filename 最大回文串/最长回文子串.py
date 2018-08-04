'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

'''


'''
解法一：暴力解法  时间复杂度o(n^3)，不贴代码了
'''

'''
解法二：动态规划 C[I][J] = 1表示是回文 ，C[I][J] = C[I+1][J-1] if 从S[I] == S[J] 否则为0 
所以动态规划应该以长度为扩展要素，也就是先解决长度短的序列，再解决长的序列
'''

def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    start = 0
    maxsize = 1
    length = len(s)
    c = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
    	c[i][i] =1
    for i in range(length-1):
    	if s[i]==s[i+1]:
    		c[i][i+1] = 1
    		if 2>maxsize and c[i][i+1] :
    			maxsize =2
    			start = i

    for l in range(2,length):
    	for i in range(length-l):
    		if s[i]==s[i+l]:
    			c[i][i+l] = c[i+1][i+l-1]
    			if l+1>maxsize and c[i][i+l]:
    				maxsize = l+1
    				start = i
    		else:
    			c[i][i+l] = 0
    return s[start:start+maxsize]



'''解法三：解法三：中心扩展法

中心扩展就是把给定的字符串的每一个字母当做中心，向两边扩展，这样来找最长的子回文串。算法复杂度为O(N^2)。
但是要考虑两种情况：
1、像aba，这样长度为奇数。
2、想abba，这样长度为偶数。
'''


def longestPalindrome2(self, s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    start = 0
    maxsize = 1

    for i in range(length):
    	k=i-1
    	l=i+1
    	while k>=0 and l<length:
    		if s[k] == s[l]:
    			if l-k+1>maxsize:
    				maxsize=l-k+1
    				start = k 
    			k-=1
    			l+=1
    		else:
    			break
    for i in range(length-1):
    	k=i
    	l=i+1
    	while k>=0 and l<length:
    		if s[k] == s[l]:
    			if l-k+1>maxsize:
    				maxsize=l-k+1
    				start = k 
    			k-=1
    			l+=1
    		else:
    			break
    return s[start:start+maxsize]


'''
解法四：马拉车算法
详情请见博客：
'''

def longestPalindrome3(self, s):
	"""
	:type s: str
	:rtype: str
	"""
	p = 0
	p0=0
	length = len(s)
	Len = [1 for i in range(2*length+1)]
	tmp =[0 for i in range(2*length+3)]
	tmp[0] = '@'
	for i in range(1,2*length,2):
		tmp[i] = '#'
		tmp[i+1] = s[int(i/2)]
	tmp[2*length+1] = '#'
	tmp[2*length+2] = '*'
	for i in range(2*length+1):
		if i<=p:
			Len[i] = min(Len[2*p0-i],p-i+1)
		else:
			Len[i] =1
		while tmp[i-Len[i]] == tmp[i+Len[i]] :
			Len[i]+=1
		if i+Len[i] -1 >p:
			p=i+Len[i] -1
			p0=i
	return max(Len)-1
	# start = Len.index(max(Len))
	# start = int((start-1)/2)
	# return s[start:start+max(Len)-1]

longestPalindrome3(1,"babad")
