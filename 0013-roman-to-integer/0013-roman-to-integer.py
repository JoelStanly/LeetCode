class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        total = 0
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        hashmap = {
            "I" : ["V","X"],
            "X" : ["L","C"],
            "C" : ["D","M"]
        }
        while(i<len(s)):
            if (i<len(s)-1 and s[i] in hashmap and s[i+1] in hashmap[s[i]]):
                i += 1
                total = total + values[s[i]] - values[s[i-1]]
            else:
                total +=values[s[i]]
            i += 1
        return total