class Solution:
    def partitionString(self, s: str) -> List[str]:
        current = ""
        result ={} 

        for i in s:
            current += i
            if current not in result:
                result[current] = True
                current =""
        return list(result.keys())