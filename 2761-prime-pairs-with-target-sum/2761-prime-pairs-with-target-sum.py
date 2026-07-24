class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        # Sieve of Eratosthenes
        
        if n<=2:
            return []
        primes = [True]*(n+1)

        primes[0] = primes[1] = False

        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False
        # print(primes)
        #find pairs directly
        res = []
        for p in range(2, n//2+1):
            if primes[p] and primes[n-p]:
                    res.append([p, n-p])
        return res


            

