class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lengthCalc = []
        shift = 0
        length = 1
        for op in operations:
            length *= 2
            lengthCalc.append(length)
            if length >= k:
                break
        for i in range(len(lengthCalc)-1,-1,-1):
            half = lengthCalc[i] // 2
            if k > half:
                k -= half
                if operations[i] == 1:
                    shift += 1
        return chr((shift)%26 + ord('a'))
            