class Solution:
    def reverseString(self, s: List[str]) -> None:
        half = len(s)//2
        for i in range(half):
            s[i],s[-(i+1)] = s[-(i+1)],s[i]
        """
        Do not return anything, modify s in-place instead.
        """
        