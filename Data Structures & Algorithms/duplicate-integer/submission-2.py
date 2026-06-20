class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []
        for i in  nums:
            if i in res:
                return True
                break
            else:
                res.append(i)
        return False
                