class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        j=0
        m,n=len(word1),len(word2)
        flag=0
        res=""

        while i<m and j<n:
            if flag==0:
                res+=word1[i]
                i+=1
            else:
                res+=word2[j]
                j+=1
            flag = 1-flag

        while i<m:
            res+=word1[i]
            i+=1

        while j<n:
            res+=word2[j]
            j+=1

        return res

        