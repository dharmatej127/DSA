class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        
        while low < high:
            mid = low + (high - low) // 2
            
            count, current_sum = 1, 0
            for x in nums:
                if current_sum + x > mid:
                    count += 1
                    current_sum = x
                else:
                    current_sum += x
            if count > k:
                low = mid + 1
            else:
                high = mid
                
        return low