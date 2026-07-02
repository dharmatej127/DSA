class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        k=n-k
        stack=[]
        for ele in nums:
            while stack and ele<stack[-1] and k>0:
                stack.pop()
                k-=1
            stack.append(ele)
        
        while stack and k>0:
            stack.pop()
            k-=1
        return stack