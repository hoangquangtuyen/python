class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        
        prefix= strs[0]
        for i in range(len(prefix)):
            for j in strs[1:]:
                if i >= len(j) or j[i] != prefix[i]:
                    return prefix[:i]
        return prefix

if __name__ == '__main__':
    s= Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))