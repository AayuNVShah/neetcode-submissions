class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m!=n:
            return False
        chrs1={}
        chrs2={}
        for i in range(m):
            chrs1[s[i]] = 1 + chrs1.get(s[i],0)
            chrs2[t[i]] = 1 + chrs2.get(t[i],0)
        if len(chrs1)!=len(chrs2):
            return False
        for i in chrs1:
            if chrs1[i]!=chrs2.get(i,0):
                return False
        return True


        