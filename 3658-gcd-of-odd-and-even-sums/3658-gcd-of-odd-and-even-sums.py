class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        count2=0  
        count1=0 
        sum_even=0
        sum_odd=0
        for i in range(1,(n*2)+1):
            if i%2==0:
                count2+=1
                sum_even+=i
                if count2>=n:
                    break
            else:
                sum_odd+=i
                count1+=1
                if count1>=n+1:
                    break    
        return gcd(sum_odd,sum_even)
                    
