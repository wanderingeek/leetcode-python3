class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num]=i
        for i, num in enumerate(nums):
            diff = target-num
            diff_index = nums_dict.get(diff)
            if diff_index is None or diff_index==i:
                continue
            else:
                return [i, diff_index]