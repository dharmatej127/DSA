class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=0
        i=0
        for i in range(0,len(digits)):
            sum=digits[i]+sum*10
            if i==len(digits)-1:
                sum+=1
        s=str(sum)
        digit=[]
        for j in range(len(s)):
                digit.insert(j,int(s[j]))
        
        return digit

        