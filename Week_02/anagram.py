class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        se = set(s)

        if se == set(t):
            for i in se:    #一开始写的s,而不是se，所以时间复杂度极其高，忽略了set
                if s.count(i) != t.count(i):
                   return False
            return True
        else:
            return False
