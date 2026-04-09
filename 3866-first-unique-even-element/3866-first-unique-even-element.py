class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for i in nums:
            if i not in freq:
                if i%2==0:
                    freq[i]=1
            else:
                freq[i]+=1
        # freq1=list(sorted(freq.items(),key=lambda x:x[1]))
        # if len(freq1)==0:
        #     return -1
        # if freq1[0][1]==1:
            # return freq1[0][0]
        for i in nums:
            if i % 2 == 0 and freq[i] == 1:
                return i
        return -1

            
       
