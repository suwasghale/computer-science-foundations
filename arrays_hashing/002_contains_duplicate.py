"""
LeetCode #217. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=array)

Pattern:
    Arrays & Hash Set

Difficulty:
    Easy

Time Complexity:
    Brute Force: O(n²)
    Optimized: O(n)

Space Complexity:
    Brute Force: O(1)
    Optimized: O(n)

Key Idea:
    We only care whether a number has already appeared.
    Since no extra information (such as index or frequency) is needed,
    a Hash Set is the perfect choice.

"""

from typing import List


# ==========================================================
# Brute Force Solution
# ==========================================================


def contains_duplicate_brute_force(nums: List[int]) -> bool:
    """
    Compare every pair of elements.

    Time Complexity:
        O(n²)

    Space Complexity:
        O(1)
    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


# ==========================================================
# Optimized Solution (Hash Set)
# ==========================================================


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Store previously seen numbers in a hash set.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        seen: set[int] = set()
        
        for num in nums: 
            
            if num in seen: 
                return True
            
            seen.add(num)
            
        return False 
    
if __name__ == "__main__":

    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3]

    print("=== Brute Force Solution ===")
    print(contains_duplicate_brute_force(nums1))
    print(contains_duplicate_brute_force(nums2))
    print(contains_duplicate_brute_force(nums3))

    print()

    print("=== Optimized Solution (Hash Set) ===")

    solution = Solution()

    print(solution.containsDuplicate(nums1))
    print(solution.containsDuplicate(nums2))
    print(solution.containsDuplicate(nums3))