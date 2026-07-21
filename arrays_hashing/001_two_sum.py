"""
Leetcode #1. Two Sum (https://leetcode.com/problems/two-sum/description/)

Pattern: 
    Arrays & Hashing
    
Difficulty: 
    Easy
    
Time Complexity:
    O(n)

Space Complexity:
    O(n)

Key Idea:
    Instead of searching every pair, store previously seen numbers in a hash map.
    For each current number, compute the complement (target - num) and check
    whether it has already been seen.

"""
from typing import List

nums = [2, 7, 11, 15]
target = 9


# ==========================================================
# Brute Force Solution
# ==========================================================


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print("=== Brute Force Solution ===")
print(two_sum_brute_force(nums, target))

# Brute-force solution.
# Compare every possible pair.
# Time Complexity: O(n²)



# ==========================================================
# Optimized Solution (Hash Map)
# ==========================================================


"""
Optimized solution.
Store previously seen numbers in a hash map for O(1) lookup.

Algorithm
1. Compute the complement. (target-num)
2. Check if the complement exists.
3. Return indices if found.
4. Otherwise store the current number.
"""
print("=== Optimized Solution (Hash Map) ===")

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        
        for index, num in enumerate(nums):
            complement = target - num 
            
            if complement in seen: 
                return [seen[complement], index]
            
            seen[num] = index 


# ==========================================================
# Test Cases
# ==========================================================


if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))