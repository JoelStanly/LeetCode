class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1,-1,-1): 
            if(i == len(digits)-1):
                carry = (digits[i]+1)//10
                digits[i] = (digits[i]+1)%10
            else:
                temp = carry
                carry = (digits[i]+carry)//10
                digits[i] = (digits[i]+temp)%10
        if(carry != 0):
            digits.insert(0,carry)
        return digits