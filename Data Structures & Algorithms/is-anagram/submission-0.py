class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount={}
        tcount={}
        for i in s:
            if i in scount:
                scount[i]+=1
            else:
                scount[i]=1
        for j in t:
            if j in tcount:
                tcount[j]+=1
            else:
                tcount[j]=1
        if scount==tcount:
            return True
        else:
            return False    
        return sorted(s) == sorted(t)        