class Solution:
    def isValid(self, s: str) -> bool:
        value = []
        for i in range(0,len(s)):
            if s[i]== "(" or s[i]=="[" or s[i]=="{":
                value.append(s[i])
            elif len(value) !=0 and ((s[i]==")" and value[-1]=="(") or (s[i]=="]" and value[-1]=="[") or (s[i]=="}" and value[-1]=="{")):
                value.pop()
            else:
                return False
        return len(value) == 0