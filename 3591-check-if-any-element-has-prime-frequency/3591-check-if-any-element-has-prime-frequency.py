class Solution(object):
    def checkPrimeFrequency(self, nums):
        def dicts(nums):
            freq={}
            for i in nums:
                freq[i]=freq.get(i,0)+1
            return freq
        
          
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        def prime_dict(freq):
            for value in freq.values():
                if is_prime(value):
                    return True 
            return False
        if prime_dict(dicts(nums)):
            return True
        else: 
            return False
