class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count_prefix=0
        for word in words:
            if pref == word[:len(pref)]:
                count_prefix+=1
        return count_prefix