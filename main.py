from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    possible = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in possible:
            return [possible[complement], i]
        
        possible[num] = i

    return